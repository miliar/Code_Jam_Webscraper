import string

def add(x,y):
    x1=bin(x)
    x2=bin(y)
    x1=x1[2:]
    x2=x2[2:]
    x1=x1[::-1]
    x2=x2[::-1]
    sum0=""
    length=min(len(x1),len(x2))
    for i in range(length):
        sum0+=str(single_digit_add(int(x1[i]),int(x2[i])))
    if len(x1)>len(x2):
        sum0+=x1[length:]
    else:
        sum0+=x2[length:]
    return eval("0b"+sum0[::-1])

        
def single_digit_add(x,y):
    return 1 if x+y==1 else 0




fin=open("C-large.in",'r')
T = int(fin.readline())
result=[]
outfile=open("output.txt","w")
for case in range(1,T+1):
    number=fin.readline()
    line0 = fin.readline()
    bags=line0.split()
    sum_all=0
    min_all=1000005
    sum_binary=0
    for i in bags:
        n3=int(i)
        sum_all+=n3
        if n3<min_all:
            min_all=n3
        sum_binary=add(sum_binary,n3)
    
    if sum_binary!=0:
        f_str="NO"
    else:
        f_str=str(sum_all-min_all)
    f_str="Case #%d: %s \n" % (case,f_str)
    outfile.write(f_str)
outfile.close()            
print "done"        
