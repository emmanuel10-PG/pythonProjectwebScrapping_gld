
# le scrapping est une technique d analyse de données pour
# étudier les données envu de prendre une décision

###### scrapping d un article

from newspaper import Article
# le site de l ' article



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

