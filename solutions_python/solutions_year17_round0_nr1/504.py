#!/usr/bin/python

def flip(S,b,K):
    for i in xrange(0,K):
        if(S[b+i]=='+'):
            S[b+i]='-'
        else:
            S[b+i]='+'


T=int(raw_input())
for i in xrange(0,T):
    line=raw_input()
    S=list(line.split(' ')[0]) 
    K=int(line.split(' ')[1])

    cnt=0
    for j in xrange(0,len(S)):
        if S[j]=='-':
            if len(S)-j>=K:
                flip(S,j,K)
                cnt = cnt+1
            else:
                cnt=-1

    if(cnt>-1):
        print("Case #"+repr(i+1)+": "+repr(cnt))
    else:
        print("Case #"+repr(i+1)+": IMPOSSIBLE")
