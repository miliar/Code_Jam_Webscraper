import sys
sys.stdin = open('input', 'r')

def solve(C, F, X):
    i = 0
    tn = X / 2
    while True:
        tn1 = tn + C / (2 + i*F) - X / (2 + i*F) + X / (2 + (i + 1)*F)
        if tn1 > tn:
            return repr(tn)
        i+=1
        tn = tn1

numcases = int(sys.stdin.readline())
for casenum in range(1, numcases + 1):
    C, F, X = [float(n) for n in sys.stdin.readline().split()]
    print 'Case #' + repr(casenum) + ': ' + solve(C, F, X)
