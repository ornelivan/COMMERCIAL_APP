import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
from matplotlib import pyplot as plt
# Importer la fonction de la page d'aide
from help_page import show_help_page

# Page layout
st.set_page_config(page_title="TABLEAU DE BORD D'ANALYSE COMMERCIALE", page_icon="🌎", layout="wide")
# st.set_page_config(page_title="GUIDE D'UTILISATION - TABLEAU DE BORD D'ANALYSE COMMERCIALE", 
#                       page_icon="📊", 
#                       layout="wide")

# Streamlit theme=none
theme_plotly = None

# Vérifier si l'utilisateur est sur la page d'aide
if 'page' not in st.session_state:
    st.session_state['page'] = 'dashboard'

# Si l'utilisateur a cliqué sur le bouton d'aide, afficher la page d'aide
if st.session_state['page'] == 'help':
    show_help_page()
    # Bouton de retour au tableau de bord
    if st.button("← Retour au Tableau de Bord"):
        st.session_state['page'] = 'dashboard'
        st.experimental_rerun()
    st.stop() # Arrêter l'exécution pour ne pas afficher le tableau de bord

# Si nous sommes ici, c'est que nous sommes sur la page du tableau de bord

# Load CSS Style
try:
    with open('style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.write("Fichier style.css non trouvé. Le style par défaut sera utilisé.")

# Titre principal avec bouton d'aide
col1, col2 = st.columns([0.9, 0.1])
with col1:
    st.markdown("# 🌐 TABLEAU DE BORD D'ANALYSE COMMERCIALE")
with col2:
    # Ajouter un bouton d'aide en haut à droite
    if st.button("❓ Aide"):
        st.session_state['page'] = 'help'
        st.rerun()

# Si vous avez un module UI personnalisé, sinon commentez cette ligne
try:
    from UI import UI
    UI()
except ImportError:
    pass  # Continuer sans le module UI

# Load dataset
try:
    df = pd.read_csv('data.csv')
    # Convertir les dates en format datetime pour faciliter le filtrage
    if 'OrderDate' in df.columns:
        df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
except Exception as e:
    st.error(f"Erreur lors du chargement des données: {e}")
    st.stop()

try:
    st.sidebar.image("images/logo2.png")
except:
    st.sidebar.title("Menu")

# Filter date to view data
with st.sidebar:
    st.title("Select Date Range")
    try:
        # Dates par défaut (aujourd'hui et il y a une semaine)
        default_start = pd.Timestamp.now().date() - pd.Timedelta(days=7)
        default_end = pd.Timestamp.now().date()
        
        start_date = st.date_input(label="Start Date", value=default_start)
        end_date = st.date_input(label="End Date", value=default_end)
    except Exception as e:
        st.error(f"Erreur avec les sélecteurs de date: {e}")
        start_date = default_start
        end_date = default_end
    
    # Ajouter le bouton d'aide également dans la barre latérale pour plus de visibilité
    st.markdown("---")
    if st.button("📚 Guide d'utilisation"):
        st.session_state['page'] = 'help'
        st.rerun()

st.error(f"Indicateurs d'activité entre le [{start_date}] et le [{end_date}]")

# Compare date - Convertit les dates et s'assure qu'elles sont en format datetime
try:
    # Conversion des dates en timestamps pandas pour la comparaison
    start_date_ts = pd.Timestamp(start_date)
    end_date_ts = pd.Timestamp(end_date)
    
    # Filtrer les données par date
    df2 = df[(df['OrderDate'] >= start_date_ts) & (df['OrderDate'] <= end_date_ts)]
    
    # Si aucune donnée n'est disponible dans la plage de dates, utiliser toutes les données
    if len(df2) == 0:
        st.warning("Aucune donnée disponible pour la période sélectionnée. Affichage de toutes les données.")
        df2 = df.copy()
except Exception as e:
    st.error(f"Erreur lors du filtrage par date: {e}")
    df2 = df.copy()

# REMPLACEMENT pour dataframe_explorer
with st.expander("Filtrer l'ensemble de données Excel"):
    # Créer des filtres dynamiques basés sur les colonnes disponibles
    st.write("### Filtres")
    
    # Colonnes de filtrage disponibles
    filter_columns = []
    for col in df2.columns:
        if col in ['OrderDate', 'Region', 'City', 'Category', 'Product']:
            filter_columns.append(col)
    
    # Création de filtres dynamiques pour les colonnes sélectionnées
    if 'OrderDate' in filter_columns:
        st.subheader("Filtrer par OrderDate")
        # Cette colonne est déjà filtrée via le sélecteur de date
        
    # Créer des colonnes pour les filtres
    col_filters = {}
    filter_cols = st.columns(min(3, len(filter_columns)))
    
    col_index = 0
    for col in filter_columns:
        if col != 'OrderDate':  # Skip OrderDate car déjà géré
            with filter_cols[col_index % len(filter_cols)]:
                st.subheader(f"Filtrer par {col}")
                # Pour les colonnes non-numériques
                if df2[col].dtype == 'object' or pd.api.types.is_categorical_dtype(df2[col]):
                    # Nettoyer les valeurs nulles avant de créer la liste
                    unique_values = df2[col].dropna().unique().tolist()
                    unique_values = ["Tous"] + unique_values
                    col_filters[col] = st.selectbox(f"Sélectionnez {col}", unique_values)
                # Pour les colonnes numériques
                elif pd.api.types.is_numeric_dtype(df2[col]):
                    min_val = float(df2[col].min())
                    max_val = float(df2[col].max())
                    col_filters[col] = st.slider(f"Plage pour {col}", 
                                               min_val, max_val, 
                                               (min_val, max_val))
            col_index += 1
    
    # Appliquer les filtres sélectionnés
    filtered_df = df2.copy()
    for col, value in col_filters.items():
        if col in df2.columns:
            if value == "Tous":
                continue
            elif isinstance(value, tuple):  # Pour les sliders numériques
                min_val, max_val = value
                filtered_df = filtered_df[(filtered_df[col] >= min_val) & 
                                        (filtered_df[col] <= max_val)]
            else:  # Pour les sélecteurs catégoriels
                filtered_df = filtered_df[filtered_df[col] == value]
    
    # Afficher le dataframe filtré
    st.dataframe(filtered_df, use_container_width=True)

# Vérifier s'il y a des données à afficher
if len(filtered_df) == 0:
    st.warning("Aucune donnée ne correspond aux critères de filtrage sélectionnés.")
    st.stop()

# Graphiques et métriques
b1, b2 = st.columns(2)

# Bar chart - Avec gestion des NaN
with b1:  
    st.subheader('Produits & Quantités', divider='rainbow')
    try:
        # S'assurer qu'il n'y a pas de valeurs NaN
        chart_data = pd.DataFrame({
            "Quantity": filtered_df["Quantity"].fillna(0),  # Remplacer NaN par 0
            "Product": filtered_df["Product"].fillna("Non spécifié")  # Remplacer NaN par "Non spécifié"
        })
        
        if len(chart_data) > 0:
            # Agréger les données pour éviter les doublons
            chart_data = chart_data.groupby("Product").sum().reset_index()
            
            # Trier par quantité pour un meilleur affichage
            chart_data = chart_data.sort_values("Quantity", ascending=False)
            
            # Limitez à 10 produits pour éviter la surcharge visuelle
            if len(chart_data) > 10:
                chart_data = chart_data.head(10)
                st.info("Affichage des 10 premiers produits par quantité")
            
            bar_chart = alt.Chart(chart_data).mark_bar().encode(
                x=alt.X("Quantity:Q", title="Quantité"),
                y=alt.Y("Product:N", sort="-x", title="Produit")
            ).properties(
                height=min(300, len(chart_data) * 30)  # Hauteur adaptative
            )
            st.altair_chart(bar_chart, use_container_width=True)
        else:
            st.warning("Pas assez de données pour afficher ce graphique.")
    except Exception as e:
        st.error(f"Erreur lors de la création du graphique à barres: {e}")

# Metric cards - Avec gestion des erreurs
with b2:
    st.subheader('Métriques des données', divider='rainbow')
    
    # CSS pour les métriques personnalisées
    st.markdown("""
    <style>
        div[data-testid="stMetricValue"] {
            font-size: 24px;
            font-weight: bold;
        }
        div[data-testid="stMetricDelta"] {
            font-size: 14px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    try:
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                label="Nombre de produits en inventaire", 
                value=filtered_df["Product"].nunique(),
                delta="Articles en stock"
            )
        with col2:
            total_price = filtered_df["TotalPrice"].sum()
            median_price = filtered_df["TotalPrice"].median()
            st.metric(
                label="Somme des prix (€)", 
                value=f"{total_price:,.0f}",
                delta=f"Médiane: {median_price:,.0f}"
            )
        
        col11, col22, col33 = st.columns(3)
        with col11:
            max_price = filtered_df["TotalPrice"].max()
            st.metric(
                label="Prix maximum (€)", 
                value=f"{max_price:,.0f}",
                delta="Prix élevé"
            )
        with col22:
            min_price = filtered_df["TotalPrice"].min()
            st.metric(
                label="Prix minimum (€)", 
                value=f"{min_price:,.0f}",
                delta="Prix bas"
            )
        with col33:
            price_range = max_price - min_price
            st.metric(
                label="Plage de prix (€)", 
                value=f"{price_range:,.0f}",
                delta="Différence min-max"
            )
    except Exception as e:
        st.error(f"Erreur lors du calcul des métriques: {e}")

# Créer des visualisations seulement si toutes les colonnes nécessaires sont présentes
required_columns = ['Product', 'TotalPrice', 'Category', 'UnitPrice', 'OrderDate']
missing_columns = [col for col in required_columns if col not in filtered_df.columns]

if missing_columns:
    st.warning(f"Certaines colonnes nécessaires sont manquantes: {', '.join(missing_columns)}")
else:
    # Dot Plot et autres graphiques
    a1, a2 = st.columns(2)
    
    # Graphique en nuage de points - Avec gestion des NaN
    with a1:
        st.subheader('Produits & Prix total', divider='rainbow')
        try:
            # Nettoyer et préparer les données
            chart_data = filtered_df.copy()
            chart_data['Product'] = chart_data['Product'].fillna('Non spécifié')
            chart_data['TotalPrice'] = chart_data['TotalPrice'].fillna(0)
            chart_data['Category'] = chart_data['Category'].fillna('Non catégorisé')
            
            # Limiter le nombre de points si trop nombreux
            if len(chart_data) > 100:
                st.info("Affichage limité à 100 points de données")
                chart_data = chart_data.sample(100)
            
            scatter_chart = alt.Chart(chart_data).mark_circle(size=60).encode(
                x=alt.X('Product:N', title='Produit'),
                y=alt.Y('TotalPrice:Q', title='Prix total'),
                color=alt.Color('Category:N', title='Catégorie'),
                tooltip=['Product', 'TotalPrice', 'Category']
            ).properties(
                height=350
            ).interactive()
            
            st.altair_chart(scatter_chart, use_container_width=True)
        except Exception as e:
            st.error(f"Erreur lors de la création du nuage de points: {e}")
    
    # Graphique à barres des prix unitaires - Avec gestion des NaN
    with a2:
        st.subheader('Produits & Prix unitaire par mois', divider='rainbow')
        try:
            # Nettoyer et préparer les données
            chart_data = filtered_df.copy()
            chart_data['Product'] = chart_data['Product'].fillna('Non spécifié')
            chart_data['UnitPrice'] = chart_data['UnitPrice'].fillna(0)
            
            # Extraire le mois des dates
            chart_data['Month'] = chart_data['OrderDate'].dt.strftime('%Y-%m')
            
            # Agréger par mois et produit
            agg_data = chart_data.groupby(['Month', 'Product'])['UnitPrice'].sum().reset_index()
            
            # Limiter le nombre de produits si trop nombreux
            if agg_data['Product'].nunique() > 10:
                top_products = chart_data.groupby('Product')['UnitPrice'].sum().nlargest(10).index.tolist()
                agg_data = agg_data[agg_data['Product'].isin(top_products)]
                st.info("Affichage limité aux 10 produits les plus vendus")
            
            bar_chart = alt.Chart(agg_data).mark_bar().encode(
                x=alt.X('Month:N', title='Mois'),
                y=alt.Y('UnitPrice:Q', title='Prix unitaire total'),
                color=alt.Color('Product:N', title='Produit'),
                tooltip=['Month', 'Product', 'UnitPrice']
            ).properties(
                height=350
            )
            
            st.altair_chart(bar_chart, use_container_width=True)
        except Exception as e:
            st.error(f"Erreur lors de la création du graphique des prix unitaires: {e}")

    # Graphiques analytiques
    p1, p2 = st.columns(2)
    
    # Nuage de points personnalisable
    with p1:
        st.subheader('Analyse des caractéristiques', divider='rainbow')
        try:
            # Séparer les colonnes par type de données
            object_columns = filtered_df.select_dtypes(include=['object']).columns.tolist()
            numeric_columns = filtered_df.select_dtypes(include=['number']).columns.tolist()
            
            if object_columns and numeric_columns:
                feature_x = st.selectbox('Sélectionnez une caractéristique qualitative (axe X)', object_columns)
                feature_y = st.selectbox('Sélectionnez une caractéristique quantitative (axe Y)', numeric_columns)
                
                # Nettoyer les données pour le graphique
                plot_data = filtered_df.copy()
                plot_data[feature_x] = plot_data[feature_x].fillna('Non spécifié')
                plot_data[feature_y] = plot_data[feature_y].fillna(0)
                
                # Créer le graphique
                fig, ax = plt.subplots(figsize=(10, 6))
                
                # Utiliser un maximum de 10 couleurs différentes pour la lisibilité
                unique_products = plot_data['Product'].unique()
                if len(unique_products) > 10:
                    top_products = plot_data.groupby('Product')[feature_y].sum().nlargest(10).index.tolist()
                    plot_data.loc[~plot_data['Product'].isin(top_products), 'Product'] = 'Autres'
                    st.info("Coloration limitée aux 10 principaux produits")
                
                sns.scatterplot(
                    data=plot_data, 
                    x=feature_x, 
                    y=feature_y, 
                    hue='Product', 
                    ax=ax,
                    palette='viridis'
                )
                
                # Ajuster l'orientation des étiquettes pour éviter le chevauchement
                plt.xticks(rotation=45, ha='right')
                plt.title(f'Relation entre {feature_x} et {feature_y}')
                plt.tight_layout()
                
                st.pyplot(fig)
            else:
                st.warning("Pas assez de types de données différents pour créer ce graphique.")
        except Exception as e:
            st.error(f"Erreur lors de la création du nuage de points personnalisé: {e}")
    
    # Histogramme
    with p2:
        st.subheader('Distribution des caractéristiques', divider='rainbow')
        try:
            object_columns = filtered_df.select_dtypes(include=['object']).columns.tolist()
            
            if object_columns:
                feature = st.selectbox('Sélectionnez une caractéristique', object_columns)
                
                # Nettoyer les données
                hist_data = filtered_df.copy()
                hist_data[feature] = hist_data[feature].fillna('Non spécifié')
                
                # Compter les occurrences
                value_counts = hist_data[feature].value_counts()
                
                # Limiter le nombre de catégories pour la lisibilité
                if len(value_counts) > 15:
                    top_values = value_counts.nlargest(14).index.tolist()
                    hist_data.loc[~hist_data[feature].isin(top_values), feature] = 'Autres'
                    st.info("Affichage limité aux 15 valeurs les plus fréquentes")
                
                # Créer le graphique
                fig, ax = plt.subplots(figsize=(10, 6))
                value_counts = hist_data[feature].value_counts()
                value_counts.plot(kind='bar', ax=ax, color='skyblue')
                
                plt.title(f'Distribution de {feature}')
                plt.xlabel(feature)
                plt.ylabel('Fréquence')
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                
                st.pyplot(fig)
            else:
                st.warning("Pas de colonnes textuelles disponibles pour l'histogramme.")
        except Exception as e:
            st.error(f"Erreur lors de la création de l'histogramme: {e}")


# Bouton caché pour le lien du pied de page
if st.button("Aide", key="help-button"):
    st.session_state['page'] = 'help'
    st.experimental_rerun()
