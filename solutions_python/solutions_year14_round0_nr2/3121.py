import sys
fin = open('B-large.in')
N = int(fin.readline())
for case in range(1,N+1):
    line=fin.readline()
    array=[]
    array.append([float(x) for x in line.split()]) 
    array=array[0]
    C=array[0];
    F=array[1];
    X=array[2];
    cps=2
    t=0
    com=0
    if X <= cps:
        ans=(X/cps)
        com=1
    if X <= C:
        ans = X/cps
        com=1
    if (com==0):
        buyfarm=1    
        while(buyfarm):
            if (X-C)/cps > X/(cps+F):
                t=t+(C/cps)
                cps=cps+F
            else:
                buyfarm=0
                t=t+(X/cps)
                ans=t      
    
    print "Case #%d: %f" % (case, ans)
    