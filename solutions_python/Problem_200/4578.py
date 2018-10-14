
def tidy(N):
    best = 0
    for i in range(1, N + 1):
        prev = 0
        for r,x in enumerate(str(i)):
            if x >= prev:
                prev = x
                if len(str(i)) == r + 1:
                    best = i
            else:
                break
    return best

lines = input()
for i in range(1, lines + 1):
    n = input()
    print "Case #{}: {}".format(i, tidy(n))
