import sys

T = input()

for t, line in enumerate(sys.stdin, 1):
    M, S = line.split()
    M = int(M)
    S = map(int, S)
    
    temp = 0
    result = 0
    for i in xrange(M + 1):
        if i > temp:
            result += (i - temp)
            temp += (i - temp)
        temp += S[i]
    print 'CASE #{}: {}'.format(t, result)
