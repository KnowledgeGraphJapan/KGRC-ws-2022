import re
import glob
import json

def printSentence(filepath, df):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        print("Mr. Avator ", end="")
        for i in range(3, len(lines)):
            pro = re.split('[ \t]', lines[i])
            m = re.match(
                r'^\[([a-zA-Z]+)\][ \t\n]+(<([a-zA-Z]+)>[ \t]+\([0-9]+\))?[ \t\n]*(<([a-zA-Z]+)>[ \t]+\([0-9]+\))?',
                lines[i].lower())
            if(m is not None):
                gr = m.groups()
#                print("Char1 ", end="")
                verb = gr[0].lower()
                if(verb in df):
                    verb = df[verb]
                print(verb, end=" ")
                if (gr[2] is None):
                    print("and ", end="")
                if (gr[2] is not None):
                    print("the " + gr[2], end=" ")
                    if (gr[4] is None):
                        print("and ", end="")
                    if (gr[4] is not None):
                        print("the " + gr[4], end=" and ")
            m = re.match(
                r'^<.+>[ \t]+\[([a-zA-Z]+)\][ \t\n]+(<([a-zA-Z]+)>[ \t]+\([0-9]+\))?[ \t\n]*(<([a-zA-Z]+)>[ \t]+\([0-9]+\))?',
                lines[i].lower())
            if(m is not None):
                gr = m.groups()
#                print("Char1 ", end="")
                verb = gr[0].lower()
                if(verb in df):
                    verb = df[verb]
                print(verb, end=" ")
                if (gr[2] is None):
                    print("and ", end="")
                if (gr[2] is not None):
                    print("the " + gr[2], end=" ")
                    if (gr[4] is None):
                        print("and ", end="")
                    if (gr[4] is not None):
                        print("the " + gr[4], end=" and ")
        print("done.")

with open('replace.json') as f:
    df = json.load(f)files = glob.glob("./KGRC-RDF/Program/**/*.txt")
for filepath in files:
    printSentence(filepath)
