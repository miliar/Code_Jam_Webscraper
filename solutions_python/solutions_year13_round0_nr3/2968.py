import sys
import math
def check(n):
    n=str(n)
    l=n[::-1]
    if(n==l):
        num=int(l)
        num=math.sqrt(num)
        rem=num-int(num)
        if(rem==0.000000000):
            num=int(num)
            num1=str(num)
            rev=num1[::-1]
            if(rev==num1):
                return True
            else:
                return False

def main():
    t=int(raw_input())
    case=1
    while(t>=0):
        count=0
        st=raw_input()
        h=st.split(' ')
        lower, upper=h
        lower=int(lower)
        upper=int(upper)
        for i in range(lower, upper+1):
            if(check(i)== True):
               count=count+1
        print 'Case #%s:' % case,count
        t=t-1
        case=case+1

if __name__=='__main__':
    main()
