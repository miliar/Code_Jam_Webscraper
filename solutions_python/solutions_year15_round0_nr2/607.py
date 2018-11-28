import sys
from Queue import PriorityQueue

args = sys.argv

if len(args) < 2:
    print 'small or large?'
    exit()

inp = args[1]

out = open(inp + '_OUT', 'w')

# No change before this

def int_row():
    return map(int, raw_input().strip().split())

def print_a(A):
    B = [str(x) for x in A]
    print ','.join(B)

def solve():
    D = input()
    A = int_row()
    ans = max(A)
    for i in xrange(1, ans+1):
        ss = i
        for j in xrange(D):
            ss += A[j]/i
            if A[j] % i == 0:
                ss -= 1
        ans = min(ans, ss)
    return str(ans)

T = input()
for i in xrange(1, T+1):
    ans = 'Case #' + str(i) + ': ' + solve()
    print ans
    out.write(ans + '\n')
# No change after this

out.close()
