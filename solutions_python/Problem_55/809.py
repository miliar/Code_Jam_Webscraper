filename = "C-small-attempt0.in"

def theme_park(R,K,N,G):
    Q = range(len(G))
    profit = 0
    for r in range(R):
        k = 0
        n = 0
        while True:
            if (k+G[Q[0]])>K  or (n+1)>len(Q):
                break
            i = Q.pop(0)
            k+=G[i]
            n+=1
            Q.append(i)
        profit += k
    return profit

if __name__ == "__main__":
    input = open(filename)
    T = int(input.readline())
    for t in range(T):
        R,K,N = [int(v) for v in input.readline().split()]
        G = [int(v) for v in input.readline().split()]
        print "Case #%d: %d"%(t+1,theme_park(R,K,N,G))
