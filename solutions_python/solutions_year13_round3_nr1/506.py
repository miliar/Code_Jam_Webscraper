import math

def func(s, n):
    start = -2
    res = 0
    num = 0
    for i in range(len(s)-n+1):
        j = 0
        while j < n:
            if s[i+j] in ['a', 'e', 'i', 'o', 'u']:
                break
            j = j + 1
        if j == n:
            num = num + 1
            if start != -2:
                res = res + (i-start)*(len(s)-n-i+1)
            else:
                res = res + (i+1)*(len(s)-n-i+1)
            start = i
    return res
t = int(input())

for CASE in range(1, t+1):
    x = input().split()
    s = x[0]
    n = int(x[1])
    
    print("Case #%d: %d"%(CASE, func(s, n)))