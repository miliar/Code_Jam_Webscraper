inn=open("c:/downloads/in.in",'r')
rs=open("c:/downloads/rs.rs",'w')
T=int(inn.readline()) #number of test cases
def timee(k,C,F,X):
    y=.0
    for i in range(k):
        y=y+C/(2+i*F)
    return (y+X/(2+k*F))
        
for i in range(T):
    ls=[]
    s=inn.readline()
    l=s.split()
    C=float(l[0])
    F=float(l[1])
    X=float(l[2])
    bound=X/C-1.0-2/F
    bound=int(bound)+1
    y=min([X/2]+[C/2+X/(2+F)]+[timee(k,C,F,X) for k in range(1,bound+1)])
    rs.write("Case #"+str(i+1)+": "+str(y)+'\n')
    
inn.close()
rs.close()
