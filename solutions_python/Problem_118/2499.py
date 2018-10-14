######################################################################
### https://code.google.com/codejam/contest/2270488/dashboard#s=p2 ###
######################################################################
def is_palindrome(x):
    global pal
    if x in pal:
        return True
    else:
        n=str(x)
        l=len(n)
        if l==1:
            pal.add(x)
            return True
        else:
            p=0
            for i in xrange(0,l/2):
                if n[i] != n[l-1-i]:
                    p=1
                    break
            if p==0:
                pal.add(x)
                return True
            else:
                return False
def fairsquare(a,b):
    import gmpy2
    global fns
    ans=0
    for i in xrange(a,b+1):
        if i in fns:
            ans+=1
        else:
            if is_palindrome(i):
                if gmpy2.is_square(i):
                    s=int(gmpy2.sqrt(i))
                    if is_palindrome(s):
                        fns.add(i)
                        ans+=1
    return ans
cases=int(raw_input())
fns=set()
pal=set()
for z in xrange(cases):
    a,b=map(int, raw_input().split())
    print "Case #"+str(z+1)+": "+str(fairsquare(a,b))