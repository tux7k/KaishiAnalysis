from time import sleep
import requests
import urllib.parse
import json # maybe unnecessary
import tqdm

# open file (exported as notes with no checkboxes)
with open('Kaishi 1.5k2.txt', 'r') as file:
    deck = file.read()

# split each line
lines = deck.splitlines()

# parse each card as word/definition
cards = []
for line in lines:
    tab_split = line.split('\t')
    if len(tab_split) > 2:
        cards.append([tab_split[0], tab_split[2]])
cards.pop(0) # correct for kaishi intro card

# cards = cards[:-1490] # delete last 1490 words to not overload jisho on demo runs
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
none = 0
research = [] # dataset after its done for further research
# scan cards for JLPT level
for index, value in tqdm.tqdm(enumerate(cards)):
    url = "https://jisho.org/api/v1/search/words?keyword=" + urllib.parse.quote(value[0])
    r = requests.get(url = url)
    try:
        json_out = r.json()
        jlpt = json_out['data'][0]['jlpt']
    except:
        print("Error... output from Jisho: ", r.text)
    research.append([value, index, jlpt])
    if len(jlpt) > 0:
        level = jlpt[-1]
        if level == "jlpt-n1":
            n1 += 1
        elif level == "jlpt-n2":
            n2 += 1
        elif level == "jlpt-n3":
            n3 += 1
        elif level == "jlpt-n4":
            n4 += 1
        elif level == "jlpt-n5":
            n5 += 1
    else:
        none += 1
    sleep(0.5)

print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(none)
print(research)