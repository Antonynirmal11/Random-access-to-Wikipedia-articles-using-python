import wikipedia
import webbrowser
def wiki():
    wikipage=wikipedia.random(1)
    wikiload=wikipedia.page(wikipage)
    s=wikipedia.summary(wikipage)
    url=wikiload.url
    print("\n\nArticle name: {} \n".format(wikipage))


    choice=input("Are you interested in this Article {}? y/n/q:").lower().strip()
    if(choice=='y' or choice=="yes"):
        print("....................summary....................\n")
        print(s)
        it=input("Do you see it in webpage? y/n:" )
        if(it=='y'):
            webbrowser.open(url)
        elif(it=='n' or it=='no'):
            wiki()
    elif(choice=='n' or choice=='no'):
        wiki()
    elif(choice=='q' or choice=='quit'):
        exit(0)
wiki()

