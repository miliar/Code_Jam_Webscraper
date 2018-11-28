#!/usr/bin/python

# google code jam - c.durr - 2012

# Speaking in Tongues
# trouver un couplage sur {a...z}


from string import *

def readint():    return int(raw_input())

clear = """a zoo
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

cyph = """y qee
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

t = maketrans(clear+cyph, cyph+clear)

for test in range(readint()):
    print "Case #%i:"% (test+1), raw_input().translate(t)
    
    
    
