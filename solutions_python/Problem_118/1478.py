def is_square(n):
    if isqrt(n)**2 == n:
        return True
    return False

def isqrt(n):
    x = 2**(sum(divmod(n.bit_length(), 2)))
    while True:
        y = (x + n//x) // 2
        if y >= x:
            return x
        x = y

def is_palin(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

def is_fair_and_square(n):
    sqr = isqrt(n)
    if sqr*sqr == n and is_palin(n) and is_palin(sqr):
        return True
    return False

t = int(input())
tests = []
for i in range(0, t):
    a = list(int(c.strip()) for c in input().split())
    tests.extend(a)
amin = min(tests)
bmax = max(tests)
is_squarepal = []
for i in range(amin, bmax+1):
    is_squarepal.append(is_fair_and_square(i))

for i in range(0, t):
    print('Case #%i: %i' %\
          (i+1, sum(x for x in is_squarepal[tests[2*i]-amin:tests[2*i+1]+1-amin])))
