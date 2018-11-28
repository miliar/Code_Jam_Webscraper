def solve(n, k):
    spaces = [(0, n)]
    while k != 0:
        space_0 = spaces[0]
        pos = space_0[0] + (space_0[1] - 1) // 2
        space_1 = space_0[0], pos-space_0[0]
        space_2 = pos+1, space_0[0]+space_0[1]-pos-1

        del spaces[0]
        if space_1[1] != 0:
            spaces.append(space_1)
        if space_2[1] != 0:
            spaces.append(space_2)
        spaces = sorted(spaces, key=lambda x:x[1], reverse=True)
        k -= 1
    a, b = pos-space_0[0], space_0[0]+space_0[1]-pos-1
    return max(a,b), min(a,b)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]
    y, z = solve(n, k)
    print "Case #{}: {} {}".format(i, y, z)
