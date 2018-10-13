import math

def sqpal():
    f=open('C-small-attempt0.in','r')
    cases=int(f.readline())
    for i in xrange(cases):
        s=0
        a=f.readline()
        for j in range(len(a)):
            if a[j]==' ':
                b=int(a[j+1:-1])
                a=int(a[:j])
                break
        for j in range(int(math.floor(math.sqrt(a))),int(math.floor(math.sqrt(b)))+1):
            if palindrome(j) and palindrome(j**2) and a<=j**2 and j**2<=b:
                s=s+1
        print 'Case #'+str(i+1)+': '+str(s)

def palindrome(x):
    x=str(x)
    n=len(x)
    for i in range(n):
        if x[i]!=x[n-i-1]:
            return False
    return True

sqpal()
