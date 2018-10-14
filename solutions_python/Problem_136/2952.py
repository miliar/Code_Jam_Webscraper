f=open('B-large.in','r')
ww=open('2nd.txt','w+')
line1=int(f.readline())

a=[]

q=0

for i in range (0,line1):
    
    b=f.readline().strip()
    a=b.split()
    t=0.0
    k=2.0
    
    
    C=float(a[0])
    F=float(a[1])
    X=float(a[2])


    while  (X-C)/k > X/(k+F):

        t +=(C/k)
        k +=F
    r=str("%.7f"%(t+X/k))
    q+=1
    j=str(q)
    ww.writelines("Case #"+j+": "+r+"\n")
    
