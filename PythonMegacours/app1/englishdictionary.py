import json
from difflib import SequenceMatcher,get_close_matches


data =json.load(open("D:\\vscode\\udemycourse\\ardit\\code\\app1\\data\\JSON+Data+Inside\\data.json"))

def translate(w):
    w=w.lower()
    closest_word=get_close_matches(w,data.keys())[0] if get_close_matches(w,data.keys()) else None
    if w in data:
        return(data[w])
    elif w.title() in data:
        return(data[w.title()])
    elif w.upper() in data:
        return(data[w.upper()])
    elif closest_word :
        yn=input('Did you mean "{}" instead ? Enter Y if Yes or N if No : '.format(closest_word)).upper()
        if yn=='Y':
            return(data[closest_word])
        elif yn=='N':
            return("word doesn't exists")
        else :
            return("We didnt understand your query")
    else :
        return("Word doesn't exists")


if __name__ == "__main__":
    word=input("enter the word: ")
    output=translate(word)
    if type(output)==list:
        print(*[str(i+1)+'. '+j for i,j in enumerate(output)],sep='\n')
    else:
        print(output)
