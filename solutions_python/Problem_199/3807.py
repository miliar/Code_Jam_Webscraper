i=int(input())
for test in xrange(i):
    l=raw_input().split()
    k=int(l[-1])
    s=list(l[0])
    j=0
    c=0
    f=0   
    for ch in xrange(len(s)-(k-1)):
        if s[ch] == "-":
            for ip in xrange(k):
                if s[ch+ip]== "-":
                    s[ch+ip]= "+"
                else:
                    s[ch+ip]= "-"
                
            c=c+1
    ak=s[ch:]
    for ii in ak:
        if ii=="-":
            f=1
    if f==1:     
        print"Case #%d: IMPOSSIBLE "%((test+1))
    else:
        print"Case #%d: %d"%((test+1),c)
            
