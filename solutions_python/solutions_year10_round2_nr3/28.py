pre_p = [
    [0],
    [1, 0],
    [0, 1, 0],
    [0, 1, 1, 0]
]

##pre_p[i][j]:::
##    how many groups of size j there are in which i is pure?
import math

def over(n, k):
    if n < k:
        return 0
    else:
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


__C = {}
def c_over(n, k):
    if (n, k) in __C:
        return __C[n, k]
    else:
        t = over(n, k)
        __C[n, k] = t
        return t
    
for n in range(4, 501):
    t = [0, 1]

    for L in range(2, n - 1):
        x = 0
        for s in range(1, L):
            x += (pre_p[L][s] * c_over(n - L - 1, L - s - 1))
        t.append(x)
    t.extend([1, 0])
    pre_p.append(t)
##    print n
    

def parse_input_and_output(infile, outfile):
    lines = open(infile).readlines()
    T = int(lines[0])
    cnt = 1
    R = []
    for i in range(T):
        try:
            t = lines[cnt]
            n = int(t)
            
            R.append("Case #%d: %d" % (i + 1, sum(pre_p[n]) % 100003))
            
            cnt += 1
        except (IndexError, ValueError):
            pass
    open(outfile, "w").write("\n".join(R))
