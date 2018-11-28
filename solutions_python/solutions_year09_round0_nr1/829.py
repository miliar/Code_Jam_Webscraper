#!/usr/bin/env python
import sys,copy
def rl(): return sys.stdin.readline().strip()

def possib(w, d):
    for word in d:
        if word[:len(w)] == w:
            return True
    return False
#L D N
T=map(int, rl().split(" "))
d=[]
n=[]
for i in range(0,T[1]):
    d.append(rl())

state=0
case=1
for line in sys.stdin:
    l=line.strip()
    wrd=[]
    cn=0
    for c in l:
        if(c=="("):
            state=1
            wrd.append("")  
        elif(c==")"):
            state=0
            cn+=1
        elif(state==1):
            wrd[cn]+=c
        elif(state==0):
            wrd.append(c)
            cn+=1
    wordlist=[""]
    for cs in wrd:
        wordcopy=[]
        for c in cs:
            for word in wordlist:
                if possib(word+c, d):
                    wordcopy.append(word+c)
        wordlist=copy.deepcopy(wordcopy)
    ans=[]
    for word in wordlist:
        if word in d:
           ans.append(word)

    print("Case #"+str(case)+": "+str(len(ans)))
    case+=1
