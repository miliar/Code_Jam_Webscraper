import math
def init(n):
    s = [0] * (n + 1)
    for i in xrange(1, n+1):
        s[i] = s[i - 1] + int(check(i))
    return s
def is_pa(n):
    s = str(n)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
def check(n):
    return is_pa(n) and is_pa(n*n)

s = init(10**7)
# print s[:10]
for t in xrange(int(raw_input())): 
    a, b = map(int, raw_input().split())
    s1 = s[int(math.sqrt(a - 1))]
    s2 = s[int(math.sqrt(b))]
    print('Case #{}: {}'.format(t + 1, s2 - s1))
