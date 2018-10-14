import sys

args = sys.argv

if len(args) < 2:
    print 'small or large?'
    exit()

inp = args[1]

out = open(inp + '_OUT', 'w')

def float_row():
    return map(float, raw_input().split())

# No change before this

def is_bigger(A, B):
    res = True
    for i in xrange(len(A)):
        if A[i] < B[i]:
            res = False
            break
    return res

def correct(A, B):
#    print 'Correct'
    X = A[:]
    Y = B[:]
    idx = 0
    while X and not X[0] > Y[-1]:
#        print X, Y
        x = X.pop(0)
        while Y[idx] < x:
            idx += 1
        Y.pop(idx)
    return str(len(X))

def incorrect(A, B):
#    print 'Incorrect'
    X = A[:]
    Y = B[:]
    while X and not is_bigger(X, Y):
#        print X, Y
        X.pop(0)
        Y.pop(-1)
    return str(len(X))

def solve():
    N = input()
    A = float_row()
    B = float_row()
    A.sort()
    B.sort()
    return '{0} {1}'.format(incorrect(A, B), correct(A, B))

T = input()
for i in xrange(1, T+1):
    ans = 'Case #' + str(i) + ': ' + solve()
    print ans
    out.write(ans + '\n')
# No change after this

out.close()
