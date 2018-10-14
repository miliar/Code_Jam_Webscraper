import sys
import gmpy2

f = open("C-small-attempt0.in", "r")
out = open("out.txt", "w")

n = int(f.readline().strip())

def pal(i):
    s = str(i)
    n = len(s)
    if n % 2 == 0:
        m = n//2
    else:
        m = n//2+1
    return s[:m] == ''.join(reversed(s[-m:]))

for i in range(n):
    a, b = map(int,f.readline().strip().split())
    count = 0
    for j in range(a,b+1):
        if pal(j) and gmpy2.is_square(j) and pal(gmpy2.isqrt(j)):
            count += 1
    out.write("Case #{}: {}\n".format(i+1, count))
out.close()
