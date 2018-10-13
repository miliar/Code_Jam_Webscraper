import re

fd  = open("input")
d = fd.read().split("\n")


L,D,N = map(int,d[0].split(" "))




dictionary = []
for i in xrange(1,D+1):
    dictionary.append(d[i])

for i in xrange(D+1,D+N+1):
    c = 0
    r = d[i].replace("(","[").replace(")","]")
    for word in dictionary:
        if re.match(r,word):
            c+=1

    print "Case #%d: %d"%(i-D,c)

