import sys


def test(R, K, N, G):
    case = 0
    last = -1
    s = 0
    for i in G:
        s += i
    if s <= K:
        return s * R

#    print s
    for r in xrange(R):
        total = 0
        i = last
        while total <= K:
            i = (i+1) % N
#            print last, i, total
            if last == i:
                break

            if total + G[i] > K:
                break

#            print 'add i', G[i]
            total += G[i]
#        print
        last = i-1

        case += total

    return case

if __name__ == "__main__":
    fileIn = sys.stdin
    T= int(fileIn.readline())

    for t in xrange(1,T+1):

        R, K, N = fileIn.readline().split()
        G = fileIn.readline().split()

        R, K, N  = int(R), int(K), int(N)
        for x in xrange(len(G)):
            G[x] = int(G[x])


        print "Case #%d:" % t,
        print test(R,K,N,G)




