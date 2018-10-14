import math

def isPalindrome(s):
    strS = str(s)
    return strS == strS[::-1]

def binSearch(n, fns, incl = True):
    start, end = 0, len(fns)
    while (end - start > 1):
        mid = divmod(start + end, 2)[0];
        if (n < fns[mid]):
            end = mid
        else:
            start = mid
    if incl:
        if n <= fns[start]:
            return start
        elif end >= len(fns) or n <= fns[end]:
            return end
        else:
            return end + 1
    else:
        if n < fns[start]:
            return start
        elif end >= len(fns) or n < fns[end]:
            return end
        else:
            return end + 1
            

def preCompute():
    l = set()
    for i in range(1, 1000):
        s = str(i)
        pal1, pal2 = s+s[::-1], s[:-1]+s[::-1]
        n1, n2 = int(pal1)**2, int(pal2)**2
        if isPalindrome(n1):
            l.add(n1)
        if isPalindrome(n2):
            l.add(n2)
    for i in range(1, 2**26):
        for s in [bin(i)[2:], '2'+bin(i)[3:], bin(i)[2:-1]+'2']:
            pal1, pal2 = s+s[::-1], s[:-1]+s[::-1]
            n1, n2 = int(pal1)**2, int(pal2)**2
            if isPalindrome(n1):
                l.add(n1)
            if isPalindrome(n2):
                l.add(n2)
    return sorted(l)

def probC(n, fns):
    cnt = 0
    for i in range(0, n):
        A, B = tuple(int(n) for n in input().split())
        a, b = binSearch(A, fns), binSearch(B, fns, False)
        print("Case #%d: %d" % (i+1, b - a))
        
fns = preCompute()
n = int(input())
probC(n, fns)
