import os
charTranslation = { "y": "a",
                    "n": "b",
                    "f": "c",
                    "i": "d",
                    "c": "e",
                    "w": "f",
                    "l": "g",
                    "b": "h",
                    "k": "i",
                    "u": "j",
                    "o": "k",
                    "m": "l",
                    "x": "m",
                    "s": "n",
                    "e": "o",
                    "z": "q",
                    "v": "p",
                    "p": "r",
                    "d": "s",
                    "r": "t",
                    "j": "u",
                    "g": "v",
                    "t": "w",
                    "h": "x",
                    "a": "y",
                    "q": "z",
                    " ": " ",
                    }
def Translate(Gstring):
    translatedString = ""
    for char in Gstring:
        translatedString += charTranslation[char.lower()]
    return translatedString

input = raw_input()
input.replace("\r", "")
lines = input.split("\n")
numLines = int(lines[0])
for i in range(1, numLines+1):
    print "Case #" + str(i) + ": " + Translate(lines[i])
