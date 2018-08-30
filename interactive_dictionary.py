import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def get_meaning(w):
    w = w.lower()

    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        decide = input('Do you mean %s instead? Press Y if yes, or N if no: ' % get_close_matches(w, data.keys())[0])
        if decide.lower() == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif decide.lower() == 'n':
            return "The word doesn't exist. Please check again."
        else:
            return "We don't understand your entry."
    else:
        return "The word doesn't exist. Please check again."

word = input("Enter word: ")

results = get_meaning(word)

if type(results) == list:
    for r in results:
        print(r)
else:
    print(results)



