import re

fin="alien_l.in"
fout="alien_l.out"
f=open(fin)
strings=[re.sub("[\r\n]",'',x) for x in f.readlines()]
f.close

L,D,N=[int(x) for x in strings[0].split(' ')]

print L,D,N
words=strings[1:D+1]
patterns=strings[D+1:]
#print words
#print patterns
f=open(fout,"w")
cc=1
for p in patterns:
    #print p
    p=re.sub('\(','[',p)
    p=re.sub('\)',']',p)
    c=0
    for w in words:
        if re.search("(%s)" % p,w) is not None:
            c+=1
    f.write("Case #%s: %s\n" % (cc,c))
    cc+=1
f.close()
