#!/usr/bin/python

#
# Third time is a charm!
#
def N(): return tuple(map(int, raw_input().split()))

T = N()[0]
for t in range(1, T + 1):
    S, K = raw_input().split()
    S = list(S)
    K = int(K)
    def flip(ss):
        return map(lambda c : '+' if c == '-' else '-', ss)

    def solve(S, moves = 0):
        # print "".join(S)
        if len(S) == K:
            if S == ['-'] * K:
                return moves + 1
            elif S == ['+'] * K:
                return moves
            else:
                return None

        if len(S) < K:
            if '-' in S:
                return None
            else:
                return moves

        if S[0] == '-':
            S[:K] = flip(S[:K])
            moves += 1

        if S[-1] == '-':
            S[-K:] = flip(S[-K:])
            moves += 1

        return solve(S[1:-1], moves)

    #print "".join(S), K
    flips = solve(S)

    print "Case #%d:" % (t,),
    if flips != None:
        print flips
    else:
        print "IMPOSSIBLE"

