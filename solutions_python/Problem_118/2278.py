import sys
import math

orig_stdin = sys.stdin
orig_stdout = sys.stdout
fo = open('C.out', 'w')
fi = open('C.in' , 'r')
sys.stdout = fo
sys.stdin = fi

def ReverseNumber(n, partial=0):
        if n == 0:
            return partial
        return ReverseNumber(n / 10, partial * 10 + n % 10)
def is_square(n):
    return math.sqrt(n).is_integer()
noc = int(raw_input())
for i in range(1,noc+1):
    count = 0
    A, B = [int(x) for x in raw_input().split()]
  
    while(A<=B):
        if (is_square(A)):
           
            if (ReverseNumber(A)==A):
                sqr=int(math.sqrt(A))
                if(ReverseNumber(sqr)==sqr):
                    count=count+1
        A=A+1
    print 'Case #' + str(i) + ': '+ str(count)
 

    
sys.stdout = orig_stdout
sys.stdin = orig_stdin
fo.close()
fi.close()
