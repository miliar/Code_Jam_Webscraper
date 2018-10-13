import sys

def printResult(i, n) :
    print('Case #{0}: {1}'.format(i, n))

t = int(sys.stdin.readline())
for i in range(1, t + 1):
    n = int(sys.stdin.readline())

    if n < 10 :
        printResult(i, n)
        continue

    for j in range(len(str(n)) - 1):
        m = [int(x) for x in str(n)][::-1]
        if(m[j] < m[j + 1]) :
            n -= n % (10 ** (j + 1)) + 1

    printResult(i, n)
