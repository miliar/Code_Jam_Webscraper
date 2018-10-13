#!/usr/bin/python

import sys

lines = sys.stdin.readlines ();

googlerese = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'

normal = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

table = {}

for i in range(len (googlerese)):
    table [googlerese [i]] = normal [i]

def change (t):
    if table.__contains__(t):
        return table [t]
    else:
        return t

def translate (s):
    result = []

    for c in s:
        result.append (change (c))

    return "".join (result)

# y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
# a b c d e f g h i j e l m n o p q r s t u v y w x y q now i enow my abcs

def safe_map (a, b):
    if not table.__contains__(a):
        table [a] = b

safe_map ('e', 'o')
safe_map ('y', 'a')
safe_map ('z', 'q')
safe_map ('a', 'w')
safe_map ('w', 'x')
safe_map ('t', 'x')
safe_map ('q', 'z')

i = 1
for line in lines[1:]:
    print ("Case #" + str (i) + ": " + translate (line.strip ()))
    i = i + 1
