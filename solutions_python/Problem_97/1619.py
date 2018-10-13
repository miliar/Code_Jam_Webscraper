def changetolist(n):
    num=[]
    for i in n:
        num.append(i)
    return num
def check(n,m):
    n=str(n)
    m=str(m)
    if len(n) != len(m):
        return 0
    nlist=changetolist(n)
    mlist=changetolist(m)
    count=0
    indicator=nlist[0]
    for d in range(0,len(mlist)):
        if indicator == mlist[d]:
            count=count+1
            if n == (m[d:]+m[:d]):
                return 1
def counter(a,b):
    count=0
    for n in range(a,b):
        for m in range(n+1,b+1):
            if check(n,m) == 1:
                count=count+1
    return count
file=raw_input('Pls enter name of input file')
f=open(file,'r')
data=[]
for line in f:
    data.append(str(line))
print data
ques=data[2]
print 'ques',ques
fout=open('output.txt','w')
number=int(data[0])
for c in range(0,number):
    fout.write('Case #')
    fout.write(str(c+1))
    fout.write(': ')
    ques=data[c+1]
    ques=ques.split(' ')
    a=int(ques[0])
    b=int(ques[1])
    ans=counter(a,b)
    fout.write(str(ans))
    fout.write('\n')
    print ans
fout.close()    
 
            
            
            
