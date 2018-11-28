
c = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv q z"
n = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up z q"

c= c.replace(" ", "")
n = n.replace(" ","")

cs = []
for x in c:
    if not x in cs:
        cs.append(x)

ns = []
for x in n:
    if not x in ns:
        ns.append(x)

a =zip(ns, cs)
#import operator
#print sorted(a, key =lambda x: x[0])

k = {}
for i,x in enumerate(cs):
    k[x] =  ns[i]

#print k



import sys

get_line = lambda : sys.stdin.readline().strip()

def tr(line):
    an = []
    for c in line :
        if c == " ":
            an.append(" ")
            continue
        an.append(k[c])

    return ''.join(an)
for l in xrange(int(get_line())):
    print "Case #%d: %s" % (l+1, tr(get_line()))
