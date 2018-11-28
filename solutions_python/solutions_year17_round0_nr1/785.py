import sys
sys.stdin=open("pancake2.in","r")
sys.stdout=open("pancake2.out","w")
for t in xrange(int(raw_input())):
    s,n=raw_input().split()
    s=map(lambda x: 0 if x=='+' else 1,s)
    s+=[0]
    add=[0 for i in xrange(len(s))]
    n=int(n)
    flip = 0
    for i in xrange(len(s)-n):
        if i:add[i]+=add[i-1]
        s[i]+=add[i]
        s[i]%=2
        if s[i]:
          s[i]=0
          add[i]+=1
          flip+=1
          add[i+n]-=1
    imp = False
    for i in xrange(len(s)-n,len(s)-1):
       if i:
           add[i]+=add[i-1]
           s[i]+=add[i]
           s[i]%=2
           if s[i]:
               imp=True
    print 'Case #%d:'%(t+1),
    if imp:print 'IMPOSSIBLE'
    else:print flip
sys.stdout.close()
