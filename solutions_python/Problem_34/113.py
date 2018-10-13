import sys,re
import string
f=open( sys.argv[1])
(L,D,N)=f.readline().strip().split()
words=[]
for i in xrange(int(D)):
    words.append(f.readline().strip());
patterns=[]
for i in xrange(int(N)):
    patterns.append(f.readline().strip());
ttt = string.maketrans("()","[]")    
patterns=["^"+p.translate(ttt)+"$" for p in patterns]
for i in xrange(len(patterns)):
    r=re.compile(patterns[i])
    res=0
    for w in words:
        if r.match(w):
            res+=1
    print "Case #"+str(i+1)+": "+str(res)


