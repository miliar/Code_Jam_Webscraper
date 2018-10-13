#!/usr/bin/env python

DEBUG = 0

def main():
    C = int(raw_input().strip())
    
    for c in range(C):
        result = 'IMPOSSIBLE'

        N, K, B, T = [int(x) for x in raw_input().split()]
        X = [int(x) for x in raw_input().split()]
        V = [int(x) for x in raw_input().split()]
        used = [0 for x in range(N)]

        if DEBUG:
            print N, K, B, T, X, V,
            print "%d of %d chicks must get to %d before t=%d" % (K, N, B, T)

        last_through = N
        n_swaps = 0
        while (N-last_through) < K:
            last_last_through = last_through
            if DEBUG: print "%d through so far (last_through=%d), need %d" % (N-last_through, last_through, K)
            # find the first one that's capable of getting through
            fastest = None
            for i in range(last_through-1, -1, -1):
                if not used[i] and X[i] + T * V[i] >= B:
                    if DEBUG: print "%d could make it" % i
                    fastest = i
                    break
            if fastest is None:
                break # impossible
            if DEBUG: print "\ttrying with %d" % i
            if i == last_through-1:
                if DEBUG: print "\tnobody in front"
            swaps_needed = last_through - 1 - i
            if DEBUG: print "\tthey'll need %d swaps" % swaps_needed
            n_swaps += swaps_needed
            last_through -= 1
            used[i] = 1
            
            if last_last_through == last_through:
                print "stopping because no progress"
                break
        if (N-last_through) >= K:
            result = str(n_swaps)

        print "Case #%d: %s" % (c+1, result)
        if DEBUG: print

main()
