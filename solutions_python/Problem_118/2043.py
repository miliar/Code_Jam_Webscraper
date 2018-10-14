def isSquare(apositiveint):
  x = (1 + apositiveint) // 2
  while apositiveint < x*x:
      x = (x + apositiveint//x) // 2
  return x*x == apositiveint

def isPal(d):
    s = str(d)
    return all(s[i]==s[-i-1] for i in range(len(s)//2))

def genPal(A,B): 
    for l in range(len(str(A)), len(str(B))+1):
        if l==1:
            for i in range(1,10):
                if A<=i<=B:
                    yield i
        elif l%2:
            for s in map(str,range(10**(l//2-1),10**(l//2))):
                for s2 in '0123456789':
                    p = int(s+s2+s[::-1])
                    if A<=p<=B:
                        yield p
        else:
            for s in map(str,range(10**(l//2-1),10**(l//2))):
                p = int(s+s[::-1])
                if A<=p<=B:
                    yield p


fairAndSquare = tuple(i*i for i in range(1,10**7) if isPal(i) and isPal(i*i))
    
t, T = 0, int(input())
while t != T:
    t += 1

    A, B = tuple(map(int, input().split()))
    
    print("Case #%d:" % t, sum(1 for i in fairAndSquare if A<=i<=B))          
