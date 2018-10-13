import sys, operator

f = map(str.strip, open(sys.argv[1], 'rb').readlines(), "\n")
n = int(f.pop(0))

def solve(c):
    if reduce(operator.xor, c) == 0: return sum(sorted(c)[1:])
    else: return "NO"

for i in range(n):
    candy = map(int, f[i*2+1].split())
    print "Case #%s: %s" % (i+1, solve(candy))
