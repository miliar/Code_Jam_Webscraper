import math
fin=open("tidy.in","r")
fout=open("tidy.out","w")
T=int(fin.readline())
def F(x):
    if x<10:
        return x
    y=x/10
    d=x%10
    z=F(y)
    if z<y:
        return 10*z+9 # if the first batch of digits must decreases, add a 9
    if y%10 <= d:
        return x
    return F(y-1)*10 + 9
    
for dummy in range(T):
    fout.write("Case #"+str(dummy+1)+": ")
    N=fin.readline().strip()
    N=int(N)
    M=F(N)
    fout.write(str(M)+'\n')
fin.close()
fout.close()
