#python3

import math

def is_palindrom(s):
    for i in range(int(len(s)/2)):
        if s[i] != s[-(i+1)]:
            return False
    return True


T = int(input())

for t in range(T):
    A, B = list(map(int, input().split()))
    
    a = int(math.sqrt(A))
    
    n = 0
    
    c = a*a
    while c <= B:
        if is_palindrom(str(a)) and is_palindrom(str(c)):
            if c >= A:
                n+=1
    
        a+=1
        c = a*a
    
    print("Case #%d: %d" % (t+1, n))


