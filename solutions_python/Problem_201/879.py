

T = int(raw_input())
for t in range(T):
    N,K = [int(i) for i in raw_input().split()]
  
    brojac=0
    d={}
    d[N]=1
    while True:
        #print d
        if brojac>=K:
            break
        a=sorted(d.keys(),reverse=True)
        duzina=a[0]
        broj=d[duzina]
        brojac+=broj
        del d[duzina]
        if duzina%2==0:
            if duzina/2-1 not in d:
                d[duzina/2-1]=broj
            else:
                d[duzina/2-1]=d[duzina/2-1]+broj
            if duzina/2 not in d:
                d[duzina/2]=broj
            else:
                d[duzina/2]=d[duzina/2]+broj
            y=duzina/2-1
            z=duzina/2
        else:
            if duzina/2 not in d:
                d[duzina/2]=2*broj
            else:
                d[duzina/2]=d[duzina/2]+2*broj
            y=z=duzina/2
   
    print "Case #%d: %d %d" % (t+1,z,y)
            
        
    
        
