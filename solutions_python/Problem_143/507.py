f = open(r"e:\downloads\b-small-attempt0.in", "r")
#f = open(r"e:\downloads\new_lottery_game.txt", "r")

T = int(f.readline())
for t in range(1, T+1):
    A, B, K  = map(int, f.readline().split())

    res = 0
    for a in xrange(A):
        for b in xrange(B):
            if (a&b) < K:
                res += 1


    print("Case #%d: %d" % (t, res))
