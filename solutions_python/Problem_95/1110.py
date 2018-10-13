#!/usr/bin/env python

Mapping = ['?'] * 256;

def Convert(fromTxt, toTxt):
    global Mapping
    for a, b in zip(fromTxt, toTxt):
        p = ord(a)
        c = ord(b)
        if Mapping[c] == '?':
            Mapping[c] = a
        elif Mapping[c] == a:
            pass
        else:
            print "Conflito: '%c', '%c', '%c'" % (a, b, Mapping[c])

def Decode(txt):
    global Mapping
    out = ""
    for a in txt:
        c = ord(a)
        #print a, Mapping[c]
        out += Mapping[c]
    return out

# so faltou uma letra no conjunto exemplo de entrada: 'z'
# que foi mapeada na letra restante 'q'

Convert(" aozq", " yeqz")
Convert("our language is impossible to understand", "ejp mysljylc kd kxveddknmc re jsicpdrysi")
Convert("there are twenty six factorial possibilities", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")
Convert("so it is okay if you want to just give up", "de kr kd eoya kw aej tysr re ujdr lkgc jv")
Sample = False
if Sample:
    print Decode("y qee")
    print Decode("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")
    print Decode("de kr kd eoya kw aej tysr re ujdr lkgc jv")
    print Decode("abcdefghijklmnopqrstuvwxyz")

testCases = int(input())
for no in range(1, testCases+1):
    toText = raw_input()
    fromText = Decode(toText)
    print "Case #%d: %s" % (no, fromText)
