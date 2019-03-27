import json
from py_translator import Translator


#File called translate.json with words to be translated, should be in json format
with open("translate.json") as f:
    words = json.load(f)

#Choose the language you want to translate to, ex. German = 'de', and input code
lan = 'en'

new_words = {}
for key,value in words.items():
    if ((key != "TS_DATE_FULL") or
        (key != "TS_DATE_LONG") or
        (key !=  "TS_DATE_MEDIUM") or
        (key != "TS_DATE_SHORT") or
        (key !=  "TS_TIME_FULL") or
        (key !=  "TS_TIME_LONG") or
        (key != "TS_TIME_MEDIUM") or
        (key !=  "TS_TIME_SHORT")):
        translated = Translator().translate(value, dest= lan).text
        new_words[key.encode('ascii', 'ignore')] = (translated.encode('ascii', 'ignore'))

#Converts dictionary to a json object
new_words = json.dumps(new_words, indent=4)

#New json file with translated text
with open("translated.json", 'w') as output:
    output.write("\"" + lan + "\"")
    output.write(": ")
    output.write(new_words)

