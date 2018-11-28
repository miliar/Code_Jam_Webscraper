from math import sqrt

def is_palin(x):
    s = str(x)
    l = len(s)
    for i in range(l/2):
        if s[i] != s[l-i-1]:
            return False
    return True

def check(x):
    #palindrome
    if is_palin(x):
        pass
    else:
        return False
    
    #square
    xx = int(sqrt(x))
    if xx*xx < x:
        return False

    return is_palin(xx)

def solve(t):
    [a, b] = [int(x) for x in raw_input().strip().split()]
    count = 0
    for x in range(a, b+1):
        if check(x):
            count += 1
            #print x
    print "Case #%d: %d" %(t, count)
    

T = int(raw_input().strip())

for t in range(1, T+1):
    solve(t)
