f=open("C:\Users\Bea\Documents\GCJ\C-small-attempt0.in.txt")
g=open("C:\Users\Bea\Documents\GCJ\C-small-attempt0.out", "w")


c=int(f.readline())
for case in range(c):
    line=f.readline()
    A,B = [int(x) for x in line.split()]
    R=0
    S=[]
    for i in range (A, B+1):
        n=len(str(i))
        p1=(i%10)*10**(n-1)+i/10
        if i<p1 and (p1 in range(A, B+1)):
            S=S+[(i,p1)]
        p2=(i%100)*10**(n-2)+i/100
        if i<p2 and (p2 in range(A, B+1)):
            S=S+[(i,p2)]
    set(S)    
 
    g.write("Case #"+str(case+1)+": "+str(len(S))+'\n')

f.close()
g.close()
