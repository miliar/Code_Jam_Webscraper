import math
def split(num):
    num1=0
    num2=0
    if num % 2 == 1:
        num1=(num - 1) / 2
        num2=num1
    else:
        num1=num/ 2
        num2=(num -1) / 2
    return str(num1) + " " +str(num2)

def process(line):
    vals=list(map(int, line.split()))
    N=vals[0]
    k=vals[1]
    num=N
    l=pow(2,int(math.log(k,2)))
    for i in range(1,int(math.log(k,2)+1)):
        num=num / 2
    if (k - l ) > (N - (num * l)):
        return split(num-1)
    else:
        return split(num)
with open('C1.in') as ins:
    count=int(ins.readline())
    for i in range(1,count+1):
        line = ins.readline()
        print "Case #"+str(i)+": "+process(line.strip())
