import re
from pprint import pprint

t="welcome to code jam"

fin="welcome_s.in"
fout="welcome_s.out"
f=open(fin)
strings=[re.sub("[\r\n]",'',x) for x in f.readlines()]
f.close()

def fint_letter(string,l):
    pass

def count(i,string):
    #if i>=len(t):
    #    return 0
    if len(t)-i>len(string):
        return 0
    if len(string)==0:
        return 1
    if i==len(t):
        return 1
    cnt=0
    c=t[i]
    s=string
    c1=0
    pos=s.find(c)
    while pos>=0:
        cnt+=count(i+1,s[pos+1:])
        s=s[pos+1:]
        pos=s.find(c)
    return cnt

f=open(fout,'w')
n=1
#print count(0,'welcome to code jamm')
for s in strings[1:]:
    ppp=str(count(0,s))[-4:]
    d=len(ppp)
    if d<4:
        ppp='0'*(4-d)+ppp
    f.write('Case #%s: %s\n' % (n,ppp))
    n+=1
