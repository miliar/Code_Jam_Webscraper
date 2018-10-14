import sys
if len(sys.argv) > 1:
    entrada = open(sys.argv[1])
else:
    entrada = open('a.in')
T = int(entrada.readline())

for caso in xrange(1, T + 1):
    linea = entrada.readline().strip()
    S, k = linea.split(' ')
    k = int(k)
    S = [x == '+' for x in S]

    flips = 0
    for i in xrange(len(S)):
        if S[i]:
            continue
        flips += 1
        if i + k > len(S):
            flips = "IMPOSSIBLE"
            break
        for j in xrange(i, i + k):
            S[j] = not S[j]
    print "Case #{}: {}".format(caso, flips)
