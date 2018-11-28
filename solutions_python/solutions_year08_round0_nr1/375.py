#!/usr/bin/python
  
n = int(raw_input())
for i in range(1, n+1):
    es=int(raw_input())
    e=[]
    saw=[]
    ans=0
    for j in range(es):
        e.append(raw_input())
        saw.append(False)
    
    ss=int(raw_input())
    for j in range(ss):
        s=raw_input()
        saw[e.index(s)] = True

        if not False in saw:
            ans+=1
            for z in range(len(saw)):
                saw[z]=False
            saw[e.index(s)] = True
        
    print "Case #%i: %i" % (i, ans)
    