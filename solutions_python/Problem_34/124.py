import re
l,d,n=map(int,raw_input().split())
word=[]
for i in xrange(d): word.append(raw_input().strip())
for i in xrange(n):
    r=raw_input()
    newr=""
    inpar=False
    for c in r:
        if c=="(":
            inpar=True
            newr+="["
        elif c==")":
            inpar=False
            newr+="]"
        else:
            newr+=c+"|"*inpar
    newr+="$"
    p=re.compile(newr)
    print "Case #"+str(i+1)+":",sum((p.match(w) is not None) for w in word)
