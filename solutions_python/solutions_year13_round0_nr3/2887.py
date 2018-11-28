import math
def check(num):
    if(str(num)[::-1]==str(num)):
        return True
    else:
        return False
def sr(num):
    if (math.sqrt(num)-int(math.sqrt(num))==0):
        return True
    else:
        return False


fin=open("C-small-attempt0.in", 'r')
fout=open("b.txt","w")
t=int(fin.readline())

for i in range(t):
    count=0
    
    x=fin.readline().split()
    a=int(x[0])
    b=int(x[1])
    for j in range(a,b+1):
        if(check(j) and sr(j)):
            if(check(int(math.sqrt(j)))):
                count=count+1
    
    fout.write("Case #"+str(i+1)+": "+str(count)+'\n')
                
fin.close()
fout.close()
