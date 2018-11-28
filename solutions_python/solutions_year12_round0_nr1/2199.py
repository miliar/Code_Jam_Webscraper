#!/usr/bin/env python

import sys
import string

inp = open(sys.argv[1], "r")
out = open("output.txt", "w+")

trans = {}
for letter in string.ascii_lowercase:
    trans[letter] = []
trans[" "] = [" "]
trans["q"] = ["z"]
    
gtext1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
gtext2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
gtext3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    
text1 = "our language is impossible to understand"
text2 = "there are twenty six factorial possibilities"
text3 = "so it is okay if you want to just give up"

for index in range(len(gtext1)):
    if text1[index] not in trans[gtext1[index]]:
        trans[gtext1[index]].append(text1[index])
    
for index in range(len(gtext2)):
    if text2[index] not in trans[gtext2[index]]:
        trans[gtext2[index]].append(text2[index])
    
for index in range(len(gtext3)):
    if text3[index] not in trans[gtext3[index]]:
        trans[gtext3[index]].append(text3[index])

alphabet = list(string.ascii_lowercase)
for letter in trans.values():
    try:
        alphabet.remove(letter[0])
    except:
        pass
    
trans["z"] = alphabet[0]

count = int(inp.next())
for index in range(count):
    gtext = inp.next().rstrip()
    text = ""
    for letter in gtext:
        text += trans[letter][0]
    out.writelines("Case #%d: %s\n" % (index+1, text))
    