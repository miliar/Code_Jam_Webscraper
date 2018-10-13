strA = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""

strB = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""

mapping={}
mapping[' ']=' '
mapping['q']='z'
mapping['z']='q'
assert(len(strA)==len(strB))
for i in xrange(len(strA)):
    if strA[i] in (' ','\n'): continue

    if strA[i] in mapping and mapping[strA[i]]!=strB[i]:
        print "discordancia :",strA[i],"->",strB[i]

    mapping[strA[i]]=strB[i]

def transform(text):
    return "".join( mapping[x] for x in text )


for i in xrange(int(raw_input())):
    print "Case #%d:"%(i+1), transform(raw_input())
