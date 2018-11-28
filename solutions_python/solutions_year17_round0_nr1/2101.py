def solve(s,k):
    l = [c=='+' for c in s]
    flips = 0
    for i in range(len(s)-k):
        if not l[i]:
            flips += 1
            for j in range(k):
                l[i+j] = not l[i+j]
    if all(l[-k:]):
        return flips
    elif not any(l[-k:]):
        return flips + 1
    else:
        return "IMPOSSIBLE"

for i in range(input()):
    s, k = raw_input().strip().split()
    k = int(k)
    print "Case #{}: {}".format(i+1,solve(s,k))
