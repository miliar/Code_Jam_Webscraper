import sys

def next_line():
    return input_file.readline().rstrip()

input_file = open(sys.argv[1])
for case in range(1, int(next_line())+1):
    print "Case #%s:" % (case),
    S, K = next_line().split()
    S = [{'+':1, '-':0}[c] for c in S]
    K = int(K)
    flips = 0
    for i in xrange(len(S)):
        if not S[i]:
            flips += 1
            if len(S) - i < K:
                print "IMPOSSIBLE"
                break
            for j in xrange(i, i + K):
                S[j] = 1 - S[j]
    else:
        print flips
