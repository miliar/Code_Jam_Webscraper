
def get_num_swaps(X, V, Tm, B, K):
    T = [(i, (B - x)/float(v)) for i, (x, v) in enumerate(zip(X, V))]
    TK = [(i, Ti) for i, Ti in T if Ti <= Tm]
    if len(TK) < K:
        return 'IMPOSSIBLE'
    TK = TK[-K:]
    
    swaps = 0
    for i, Ti in TK:
        for j, Tj in T[i+1:]:
            if Tj > Tm:
                swaps += 1
    return swaps
    

def run(f):
    case_num = int(f.readline())
    for i in xrange(case_num):
        N, K, B, T = map(int, f.readline().split())
        X = map(int, f.readline().split())[:N]
        V = map(int, f.readline().split())[:N]
        print "Case #%d: %s" % (i+1, get_num_swaps(X, V, T, B, K))

if __name__ == '__main__':
    import sys
    run(open(sys.argv[1]))