import re

s=open(raw_input('Enter filename:')).readlines()
L=int(s[0].split()[0])
D=int(s[0].split()[1])
N=int(s[0].split()[2])

words=s[1:1+D]
tests=s[1+D:1+D+N]

t=0
for test in tests:
    test=re.sub('\(','[',test)
    test=re.sub('\)',']',test)
    c=0
    for w in words:
        if re.match(test,w):
            c+=1
    t+=1
    print 'Case #'+str(t)+':',c
    
