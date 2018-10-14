import sys

def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)

# N = max D
def solve(N, pD, pG):
    minD = 100 / gcd(pD,100)
    if minD>N:
        return False
    if pG == 100 and pD < 100:
        return False
    if pG == 0 and pD > 0:
        return False
    return True

input_file = len(sys.argv)>1 and sys.argv[1] or 'input.txt'
outf = len(sys.argv)>2 and open(sys.argv[2],'w') or sys.stdout
with open(input_file) as f:
    N = int(f.readline())
    for x in range(N):
        P = map(int, f.readline().split(' '))
        outf.write('Case #{0}: '.format(x+1))
        possible = solve(*P)
        if possible:
            outf.write('Possible\n')
        else:
            outf.write('Broken\n')


