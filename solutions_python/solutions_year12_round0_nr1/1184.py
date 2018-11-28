import sys
g = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

r = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

trans = {}
for i,c in zip(range(len(g)),g):
    if trans.has_key(c) and trans[c] != r[i]:
        print 'burrrrp more than one mappa? abuuhhh?'
        #If only I could be more graceful... but now.. I.. die

        sys.exit()
    trans[c] = r[i]

trans['z'] = 'q'
trans['q'] = 'z'


inputfile = open(sys.argv[1], 'r')
cases = int(inputfile.readline())
for i in range(cases):
    outputstring = ""
    confusing = inputfile.readline()[:-1]
    for c in confusing:
        outputstring += trans[c]

    print "Case #%s: %s"%(i+1, outputstring)
