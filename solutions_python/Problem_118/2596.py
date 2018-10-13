import math
import sys


def is_square(n):
    return math.sqrt(n).is_integer()

def ReverseNumber(n, partial=0):
    if n == 0:
        return partial
    return ReverseNumber(n / 10, partial * 10 + n % 10)

inf=open(sys.argv[1],'r');
lines=inf.readlines();
T=int(lines[0]);


for i in range(0,T):
    As,Bs=lines[i+1].split(' ');
    A,B=int(As),int(Bs)
    count=0;
    for num in range(A,B+1):
        if (ReverseNumber(num) == num):
            num1=math.sqrt(num);
            if(num1.is_integer()):
                num2=int(num1)
                if(ReverseNumber(num2) == num2):
                    count+=1;
    print "Case #"+str(i+1)+": ",count;

