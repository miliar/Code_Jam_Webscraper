from operator import itemgetter, attrgetter

def output(t, res):
    casestr = "Case #" + str(t+1) +": "
    status = str(res)
    outputLine = casestr+status
    print outputLine


def main():
    T = int( raw_input() )
    for t in xrange(T):            
        A, B, K = map( int, raw_input().split() )
        s = 0
        for a in xrange(A):
            for b in xrange(B):
                s += ( (a & b) < K)
        output(t, s)


if __name__ == "__main__":
   main()