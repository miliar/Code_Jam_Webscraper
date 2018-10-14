import itertools

def solve(S):
    sums = {}
    for m in range(1, len(S)+1):
        for c in itertools.combinations(S, m):
            s = sum(c)
            if s in sums:
                return c, sums[s]
            sums[s] = c
    return None

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        S = map(int, raw_input().split())[1:]
        sol = solve(S)
        print "Case #%d:" %i
        if sol == None:
            print "Impossible"
        else:
            print " ".join(map(str, sol[0]))
            print " ".join(map(str, sol[1]))
            
