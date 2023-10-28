
# le scrapping est une technique d analyse de données pour
# étudier les données envu de prendre une décision

###### scrapping d un article

from newspaper import Article
# le site de l ' article

####

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    url = "https://timesofindia.com/topic/Donald-Trump"
    article = Article(url)

    # telecharge l article
    article.download()

    # permet de departager les infos de l article comme le titre , l entête , l a description
    article.parse()

    # afficher le titre
    print(article.title)
    print("\n")
    # afficher la description
    print(article.text)
    print("\n")


################# scrapping d avis sur google #####################################

import pandas as pd
# installation du package google_play_scraper
# pip install google_play_scraper
#  commentaire multiple en python trois cotes (   '''  lorem upsum '''   )
from google_play_scraper import reviews , reviews_all ,Sort



## scraping de commentaire d une app ( linkedin : recherche d'emplois)

url='com.linkedin.android'
avis,_ = reviews(url , lang='fr',country='ci',
    sort= Sort.MOST_RELEVANT, count= 4 )


donnees_avis_app = pd.DataFrame.from_records(avis)

# donne les entetes de structure de l api et les 2 premiers avis de l app
print(donnees_avis_app.head(2))

# donne le nombre d avis sur 10  exemple : (2 , 11 avis total)
print(donnees_avis_app.shape)

## 0 donne le premier nom avis de la partie 'userName' de l app. ( c est le tout premier nom utilisateur ayant commenté l app )
print(donnees_avis_app['userName'][0])


## donne le premier avis de la partie 'content' de l app. ( c est le tout premier commentaire de l app )

print(donnees_avis_app['content'][0])
print("\n")

## donne le premier avis de la partie 'content' de l app. ( c est le tout premier commentaire de l app )

print(donnees_avis_app['content'][2])