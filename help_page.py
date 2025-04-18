# help_page.py

import streamlit as st
import pandas as pd
from PIL import Image
import base64

def show_help_page():
    # Configuration de la page
    st.title("📚 Guide d'utilisation du tableau de bord d'analyse commerciale")
    
    # CSS pour le style de la page
    st.markdown("""
    <style>
        .main-header {
            font-size: 36px;
            font-weight: bold;
            color: #1E3A8A;
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 15px;
            border-bottom: 2px solid #3B82F6;
        }
        
        .sub-header {
            font-size: 24px;
            font-weight: bold;
            color: #1E40AF;
            margin-top: 30px;
            margin-bottom: 15px;
            padding-bottom: 5px;
            border-bottom: 1px solid #93C5FD;
        }
        
        .feature-title {
            font-size: 20px;
            font-weight: bold;
            color: #2563EB;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        
        .tip-box {
            background-color: #DBEAFE;
            padding: 15px;
            border-radius: 5px;
            border-left: 5px solid #3B82F6;
            margin-bottom: 20px;
        }
        
        .warning-box {
            background-color: #FEF3C7;
            padding: 15px;
            border-radius: 5px;
            border-left: 5px solid #F59E0B;
            margin-bottom: 20px;
        }
        
        .key-point {
            font-weight: bold;
            color: #1E40AF;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # En-tête principal
    st.markdown("<div class='main-header'>📚 GUIDE D'UTILISATION DU TABLEAU DE BORD D'ANALYSE COMMERCIALE</div>", unsafe_allow_html=True)
    
    # Introduction
    st.markdown("""
    Ce guide explique comment utiliser efficacement le tableau de bord d'analyse commerciale pour optimiser 
    vos décisions commerciales et mieux comprendre les performances de vos produits et de vos ventes.
    """)
    
    # Barre latérale pour la navigation
    with st.sidebar:
        st.title("Navigation")
        
        # Logo de l'entreprise
        try:
            st.image("images/logo2.png")
        except:
            st.write("Logo non disponible")
        
        # Menu de navigation
        page = st.radio(
            "Aller à:",
            ["Introduction", "Fonctionnalités principales", "Filtrage des données", "Interprétation des graphiques", 
             "Métriques clés", "Analyses avancées", "Astuces et bonnes pratiques", "FAQ"]
        )
    
    # Contenu principal basé sur la sélection
    if page == "Introduction":
        st.markdown("<div class='sub-header'>Introduction au tableau de bord</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            Le tableau de bord d'analyse commerciale est un outil puissant conçu pour vous aider à :
            
            - **Visualiser** les données de ventes et d'inventaire
            - **Identifier** les tendances et les opportunités
            - **Analyser** les performances des produits
            - **Prendre** des décisions commerciales éclairées
            
            Cette interface intuitive vous permet d'explorer vos données commerciales à travers différentes dimensions 
            et de générer des insights précieux pour votre stratégie commerciale.
            """)
        
        with col2:
            st.markdown("<div class='tip-box'>💡 <span class='key-point'>Conseil</span> : Commencez par définir la période d'analyse pertinente pour votre objectif commercial spécifique.</div>", unsafe_allow_html=True)
    
    elif page == "Fonctionnalités principales":
        st.markdown("<div class='sub-header'>Fonctionnalités principales</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='feature-title'>1. Sélection de plage de dates</div>", unsafe_allow_html=True)
        st.markdown("""
        - Situé dans la barre latérale gauche
        - Permet de filtrer les données par période spécifique
        - Affecte tous les graphiques et métriques du tableau de bord
        
        <div class='tip-box'>💡 <span class='key-point'>Utilisation recommandée</span> : Pour les analyses mensuelles, sélectionnez le premier et le dernier jour du mois. Pour les analyses trimestrielles, sélectionnez les trois mois consécutifs.</div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div class='feature-title'>2. Filtrage avancé des données</div>", unsafe_allow_html=True)
        st.markdown("""
        - Disponible dans la section "Filtrer l'ensemble de données Excel"
        - Permet de filtrer par région, ville, catégorie et produit
        - Offre une vue personnalisée des données selon vos besoins d'analyse
        """)
        
        st.markdown("<div class='feature-title'>3. Visualisations interactives</div>", unsafe_allow_html=True)
        st.markdown("""
        - Graphique à barres des produits et quantités
        - Nuage de points pour l'analyse produit/prix
        - Graphique de prix unitaires par mois
        - Visualisations personnalisables des caractéristiques
        
        <div class='tip-box'>💡 <span class='key-point'>Astuce</span> : Survolez les graphiques pour obtenir des informations détaillées sur chaque point de données.</div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div class='feature-title'>4. Métriques clés</div>", unsafe_allow_html=True)
        st.markdown("""
        - Nombre de produits en inventaire
        - Somme totale des prix
        - Prix maximum, minimum et plage de prix
        - Médianes et autres statistiques descriptives
        """)
    
    elif page == "Filtrage des données":
        st.markdown("<div class='sub-header'>Guide de filtrage des données</div>", unsafe_allow_html=True)
        
        st.markdown("""
        Le filtrage efficace des données est essentiel pour obtenir des insights pertinents. Voici comment utiliser 
        les différentes options de filtrage :
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<div class='feature-title'>Filtrage par date</div>", unsafe_allow_html=True)
            st.markdown("""
            1. Accédez à la barre latérale gauche
            2. Utilisez les sélecteurs "Date de début" et "Date de fin"
            3. Cliquez sur une date dans le calendrier ou saisissez-la manuellement
            
            <div class='tip-box'>💡 <span class='key-point'>Cas d'utilisation</span> : Comparez les performances d'une période avec la même période de l'année précédente pour identifier les tendances saisonnières.</div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div class='feature-title'>Filtrage par région et ville</div>", unsafe_allow_html=True)
            st.markdown("""
            1. Dépliez la section "Filtrer l'ensemble de données Excel"
            2. Utilisez les menus déroulants pour sélectionner une région ou une ville spécifique
            3. Pour annuler le filtre, sélectionnez "Tous"
            
            <div class='tip-box'>💡 <span class='key-point'>Cas d'utilisation</span> : Identifiez les régions à forte ou faible performance pour ajuster vos stratégies commerciales régionales.</div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='feature-title'>Filtrage par catégorie</div>", unsafe_allow_html=True)
            st.markdown("""
            1. Utilisez le menu déroulant "Filtrer par Category"
            2. Sélectionnez une catégorie de produit spécifique
            3. Pour voir toutes les catégories, sélectionnez "Tous"
            
            <div class='tip-box'>💡 <span class='key-point'>Cas d'utilisation</span> : Analysez les performances par catégorie pour identifier les opportunités de croissance ou les segments en difficulté.</div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div class='feature-title'>Filtrage par produit</div>", unsafe_allow_html=True)
            st.markdown("""
            1. Utilisez le menu déroulant "Filtrer par Product"
            2. Sélectionnez un produit spécifique pour une analyse détaillée
            3. Pour voir tous les produits, sélectionnez "Tous"
            
            <div class='warning-box'>⚠️ <span class='key-point'>Attention</span> : L'application de trop de filtres simultanément peut réduire considérablement l'ensemble de données, rendant certaines analyses moins significatives.</div>
            """, unsafe_allow_html=True)
    
    elif page == "Interprétation des graphiques":
        st.markdown("<div class='sub-header'>Comment interpréter les graphiques</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='feature-title'>Graphique Produits & Quantités </div>", unsafe_allow_html=True)
        st.markdown("""
        Ce graphique à barres horizontales montre les quantités vendues pour chaque produit.
        
        **Comment l'interpréter :**
        - Produits avec des barres plus longues = produits les plus vendus
        - Produits avec des barres courtes = produits à faible rotation
        
        **Actions commerciales suggérées :**
        - Pour les produits à forte demande, assurez un stock suffisant
        - Pour les produits à faible rotation, envisagez des promotions ou une réévaluation de leur pertinence
        
        <div class='tip-box'>💡 <span class='key-point'>Astuce</span> : Ce graphique est limité aux 10 premiers produits par quantité pour assurer la lisibilité. Pour une analyse complète, exportez les données brutes.</div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div class='feature-title'>Nuage de points Produits & Prix total </div>", unsafe_allow_html=True)
        st.markdown("""
        Ce graphique montre la relation entre les produits et leur prix total, avec un code couleur par catégorie.
        
        **Comment l'interpréter :**
        - Points plus haut sur l'axe Y = produits à prix plus élevé
        - Clusters de points = produits de même gamme de prix
        - Couleurs différentes = catégories de produits
        
        **Actions commerciales suggérées :**
        - Identifiez les produits à forte valeur pour des actions commerciales ciblées
        - Repérez les anomalies de prix qui pourraient nécessiter un ajustement
        
        <div class='tip-box'>💡 <span class='key-point'>Interaction</span> : Survolez les points pour voir les détails exacts de chaque produit, y compris son prix et sa catégorie.</div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div class='feature-title'>Graphique Produits & Prix unitaire par mois </div>", unsafe_allow_html=True)
        st.markdown("""
        Ce graphique à barres empilées montre l'évolution des prix unitaires par produit au fil du temps.
        
        **Comment l'interpréter :**
        - Hauteur totale des barres = prix unitaire total par mois
        - Sections colorées = contribution de chaque produit au prix unitaire total
        - Tendance à la hausse/baisse = évolution des prix unitaires dans le temps
        
        **Actions commerciales suggérées :**
        - Identifiez les mois avec des pics de prix unitaires pour comprendre les facteurs saisonniers
        - Analysez la contribution des différents produits aux variations de prix
        """)
        
        st.markdown("<div class='feature-title'>Analyse des caractéristiques personnalisable</div>", unsafe_allow_html=True)
        st.markdown("""
        Ce graphique permet d'explorer la relation entre différentes caractéristiques des données.
        
        **Comment l'utiliser :**
        1. Sélectionnez une caractéristique qualitative pour l'axe X
        2. Sélectionnez une caractéristique quantitative pour l'axe Y
        3. Observez la distribution et les relations entre ces caractéristiques
        
        <div class='warning-box'>⚠️ <span class='key-point'>Attention</span> : Les corrélations visibles ne signifient pas nécessairement une relation de cause à effet. Utilisez ces insights comme point de départ pour des analyses plus approfondies.</div>
        """, unsafe_allow_html=True)
    
    elif page == "Métriques clés":
        st.markdown("<div class='sub-header'>Comprendre les métriques clés</div>", unsafe_allow_html=True)
        
        st.markdown("""
        Les métriques clés fournissent un aperçu rapide de la performance globale de vos produits et ventes.
        Voici comment interpréter et utiliser efficacement chaque métrique :
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<div class='feature-title'>Nombre de produits en inventaire</div>", unsafe_allow_html=True)
            st.markdown("""
            **Description :** Affiche le nombre total de produits uniques dans la période sélectionnée.
            
            **Utilisation stratégique :**
            - Surveillez l'évolution de la diversité de votre catalogue
            - Comparez avec les périodes précédentes pour identifier les tendances d'expansion ou de rationalisation du catalogue
            
            <div class='tip-box'>💡 <span class='key-point'>Interprétation</span> : Une baisse significative peut indiquer des problèmes de gestion d'inventaire ou une stratégie de rationalisation du catalogue.</div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div class='feature-title'>Somme des prix (€)</div>", unsafe_allow_html=True)
            st.markdown("""
            **Description :** Représente le total des prix pour tous les produits dans la période sélectionnée.
            
            **Utilisation stratégique :**
            - Évaluez rapidement la valeur totale des ventes
            - Suivez l'évolution du chiffre d'affaires total
            - Comparez avec vos objectifs commerciaux
            
            <div class='tip-box'>💡 <span class='key-point'>Médiane</span> : La médiane affichée sous cette métrique vous indique le prix médian, utile pour identifier les gammes de prix dominantes.</div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='feature-title'>Prix maximum et minimum (€)</div>", unsafe_allow_html=True)
            st.markdown("""
            **Description :** Affiche le prix le plus élevé et le plus bas dans l'ensemble de données filtré.
            
            **Utilisation stratégique :**
            - Identifiez rapidement vos produits premium et d'entrée de gamme
            - Repérez les anomalies potentielles dans vos données de prix
            - Évaluez l'étendue de votre stratégie de tarification
            
            <div class='warning-box'>⚠️ <span class='key-point'>Vigilance</span> : Des valeurs extrêmes peuvent indiquer des erreurs de saisie de données ou des cas spéciaux qui méritent une investigation.</div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div class='feature-title'>Plage de prix (€)</div>", unsafe_allow_html=True)
            st.markdown("""
            **Description :** Représente la différence entre le prix maximum et minimum.
            
            **Utilisation stratégique :**
            - Évaluez la diversité de votre stratégie de prix
            - Identifiez si votre catalogue couvre un large éventail de segments de marché
            - Comparez avec les concurrents pour positionner votre offre
            
            <div class='tip-box'>💡 <span class='key-point'>Application pratique</span> : Une plage étroite peut indiquer une focalisation sur un segment de marché spécifique, tandis qu'une plage large suggère une approche plus diversifiée.</div>
            """, unsafe_allow_html=True)
    
    elif page == "Analyses avancées":
        st.markdown("<div class='sub-header'>Effectuer des analyses avancées</div>", unsafe_allow_html=True)
        
        st.markdown("""
        Pour tirer le maximum de valeur de ce tableau de bord, vous pouvez réaliser des analyses plus sophistiquées 
        en combinant différentes fonctionnalités. Voici quelques techniques avancées :
        """)
        
        st.markdown("<div class='feature-title'>Analyse de tendances temporelles</div>", unsafe_allow_html=True)
        st.markdown("""
        **Méthode :**
        1. Utilisez des périodes consécutives (par ex. plusieurs mois d'affilée)
        2. Notez les métriques clés pour chaque période
        3. Créez un tableau de suivi pour visualiser l'évolution
        
        **Application :**
        - Identifiez les motifs saisonniers dans les ventes de produits
        - Anticipez les pics de demande pour la planification des stocks
        - Évaluez l'impact des campagnes marketing sur les ventes
        
        <div class='tip-box'>💡 <span class='key-point'>Astuce avancée</span> : Exportez les données filtrées et utilisez Excel pour créer des graphiques de séries temporelles sur plusieurs périodes.</div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div class='feature-title'>Analyse comparative par segment</div>", unsafe_allow_html=True)
        st.markdown("""
        **Méthode :**
        1. Filtrez par un segment spécifique (région, catégorie, etc.)
        2. Notez les métriques clés
        3. Répétez pour d'autres segments
        4. Comparez les performances
        
        **Application :**
        - Comparez les performances des produits entre différentes régions
        - Identifiez les catégories les plus rentables
        - Détectez les opportunités d'expansion géographique
        
        <div class='warning-box'>⚠️ <span class='key-point'>Considération importante</span> : Tenez compte de la taille relative de chaque segment lors de la comparaison des performances absolues.</div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div class='feature-title'>Analyse de corrélation prix-quantité</div>", unsafe_allow_html=True)
        st.markdown("""
        **Méthode :**
        1. Utilisez le graphique personnalisable d'analyse des caractéristiques
        2. Sélectionnez "Product" sur l'axe X et "Quantity" sur l'axe Y
        3. Comparez avec un second graphique montrant "Product" et "UnitPrice"
        
        **Application :**
        - Identifiez si les produits à prix élevé ont tendance à avoir des volumes de vente plus faibles
        - Trouvez le "sweet spot" prix/volume pour maximiser le chiffre d'affaires
        - Détectez les produits anomaliques qui dérogent à la tendance générale
        """)
        
    elif page == "Astuces et bonnes pratiques":
        st.markdown("<div class='sub-header'>Astuces et bonnes pratiques</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<div class='feature-title'>Pour une analyse efficace</div>", unsafe_allow_html=True)
            st.markdown("""
            1. **Commencez large, puis affinez** : Commencez par examiner l'ensemble des données avant d'appliquer des filtres pour avoir une vision d'ensemble.
            
            2. **Utilisez des périodes comparables** : Pour les analyses temporelles, comparez des périodes de même durée (mois à mois, trimestre à trimestre).
            
            3. **Combinez les filtres judicieusement** : L'application de trop de filtres peut réduire excessivement l'ensemble de données.
            
            4. **Exportez les insights importants** : Prenez des captures d'écran ou notez les observations clés pour les partager avec votre équipe.
            
            5. **Vérifiez les valeurs aberrantes** : Les points de données extrêmes peuvent indiquer des opportunités ou des problèmes à résoudre.
            """)
            
            st.markdown("<div class='tip-box'>💡 <span class='key-point'>Conseil</span> : Établissez une routine d'analyse hebdomadaire ou mensuelle pour suivre systématiquement les performances.</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='feature-title'>Erreurs courantes à éviter</div>", unsafe_allow_html=True)
            st.markdown("""
            1. **Tirer des conclusions à partir d'échantillons trop petits** : Assurez-vous d'avoir suffisamment de données pour que l'analyse soit significative.
            
            2. **Ignorer le contexte saisonnier** : Certaines variations sont normales selon la période de l'année.
            
            3. **Négliger les médianes au profit des moyennes** : Les moyennes peuvent être faussées par des valeurs extrêmes.
            
            4. **Sur-interpréter les corrélations** : Une corrélation n'implique pas nécessairement une causalité.
            
            5. **Oublier de réinitialiser les filtres** : Assurez-vous de réinitialiser tous les filtres avant de commencer une nouvelle analyse.
            """)
            
            st.markdown("<div class='warning-box'>⚠️ <span class='key-point'>Attention</span> : N'oubliez pas que les données ne racontent qu'une partie de l'histoire. Combinez toujours l'analyse quantitative avec votre connaissance du marché et du contexte commercial.</div>", unsafe_allow_html=True)
    
    elif page == "FAQ":
        st.markdown("<div class='sub-header'>Foire Aux Questions</div>", unsafe_allow_html=True)
        
        # Utilisation d'expanders pour les FAQ
        with st.expander("Comment puis-je exporter les données filtrées pour une analyse externe ?"):
            st.markdown("""
            Bien que le tableau de bord ne dispose pas d'une fonction d'exportation intégrée, vous pouvez :
            
            1. Utiliser la fonctionnalité de copie du tableau de données affiché
            2. Faire un clic droit sur le tableau et sélectionner "Copier"
            3. Coller les données dans Excel ou un autre outil d'analyse
            
            Pour les graphiques, vous pouvez utiliser des captures d'écran pour les inclure dans vos rapports.
            """)
        
        with st.expander("Pourquoi certains graphiques affichent-ils un message indiquant que l'affichage est limité ?"):
            st.markdown("""
            Pour des raisons de performance et de lisibilité, certains graphiques limitent automatiquement le nombre d'éléments affichés :
            
            - Le graphique à barres des produits est limité aux 10 premiers produits par quantité
            - Le nuage de points est limité à 100 points de données
            - L'histogramme est limité aux 15 valeurs les plus fréquentes
            
            Ces limitations sont en place pour garantir que les visualisations restent compréhensibles et que l'application reste performante.
            """)
        
        with st.expander("Les données semblent incorrectes ou incomplètes, que faire ?"):
            st.markdown("""
            Si vous suspectez des problèmes avec les données :
            
            1. Vérifiez que le fichier de données source (data.csv) est à jour et correctement formaté
            2. Assurez-vous que les dates sont au format correct (YYYY-MM-DD)
            3. Vérifiez que vous n'avez pas appliqué de filtres trop restrictifs
            4. Redémarrez l'application si nécessaire
            
            Si le problème persiste, contactez l'équipe informatique en mentionnant spécifiquement les incohérences observées.
            """)
        
        with st.expander("Comment puis-je analyser les performances d'un nouveau produit ?"):
            st.markdown("""
            Pour analyser un nouveau produit récemment ajouté au catalogue :
            
            1. Utilisez le filtre "Filtrer par Product" pour sélectionner spécifiquement ce produit
            2. Examinez ses métriques de performance sur la période disponible
            3. Comparez avec des produits similaires en utilisant l'analyse des caractéristiques
            4. Analysez son évolution des prix et des quantités au fil du temps
            
            Pour les produits très récents, notez que les données peuvent être limitées, ce qui rend certaines analyses moins fiables.
            """)
        
        with st.expander("Est-il possible de personnaliser davantage le tableau de bord pour mon équipe ?"):
            st.markdown("""
            Le tableau de bord peut être adapté aux besoins spécifiques de votre équipe. Contactez l'équipe de développement pour discuter des possibilités de personnalisation, telles que :
            
            - Ajout de nouvelles visualisations
            - Intégration de sources de données supplémentaires
            - Création de filtres personnalisés
            - Implémentation de KPIs spécifiques à votre équipe
            
            Notez que les personnalisations substantielles peuvent nécessiter un temps de développement supplémentaire.
            """)
    
    # Pied de page
    st.markdown("---")
    st.markdown("""
    
    """, unsafe_allow_html=True)

# Fonction pour créer un bouton de retour à l'analyse
def back_to_dashboard():
    st.rerun()
    st.markdown("""
    <div style="margin-top: 20px;">
        <a href="/" style="text-decoration: none;">
            <button style="
                background-color: #3B82F6;
                color: white;
                padding: 10px 15px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-weight: bold;
                display: flex;
                align-items: center;
                width: fit-content;
            ">
                ← Retour au Tableau de Bord
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
    st.rerun()

# Si cette fonction est appelée directement
if __name__ == "__main__":
    show_help_page()
    back_to_dashboard()