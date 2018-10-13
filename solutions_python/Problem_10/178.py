import sys

def optimize(P,K,L,letter_freq):
    keys = [[] for i in xrange(K)]
    k = 0
    letter_freq.sort()
    for x in xrange(L):
        keys[k].append(letter_freq.pop())
        k += 1
        k %= K
    sum = 0
    for x in keys:
        for i, c in enumerate(x):
            sum += (i+1)*c
    return sum

def main ():
    cases = int(sys.stdin.readline())
    for x in xrange(cases):
        P, K, L = [int(i) for i in sys.stdin.readline().split()]
        letter_freq = [int(i) for i in sys.stdin.readline().split()]
        print "Case #%s: %s" % (x+1, optimize(P,K,L,letter_freq))
    return 0

if __name__ == "__main__":
    status = main()
    sys.exit(status)
