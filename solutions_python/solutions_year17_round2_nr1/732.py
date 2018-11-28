def do_case(i):
    D, N = map(int, raw_input().split())
    K=[]
    S=[]
    T=[]
    for j in xrange(N):
        k, s = map(int, raw_input().split())
        K.append(k)
        S.append(s)
        T.append((D-k)/float(s))
    V = float(D) / max(T)
    print "Case #{}: {}".format(i+1, V)

def main():
    N = int(raw_input())
    for i in xrange(N):
        do_case(i)

main()

