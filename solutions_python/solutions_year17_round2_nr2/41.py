import sys
import operator
sys.stdout = open('b.out', 'w')
sys.stdin  = open("b.in", 'r')
sys.setrecursionlimit(1500)

def algorithm_small(N, R, O, Y, G, B, V):
    if R > N/2 or Y > N/2 or B > N/2:
        return "IMPOSSIBLE"
    colors = {"R": R, "B": B, "Y": Y}

    div = max(colors.iteritems(), key=operator.itemgetter(1))[0]

    barn = [None] * N

    i = 0
    while colors[div] > 0:
        barn[i] = div
        colors[div] -= 1
        i += 2

    del colors[div]
    for i in range(N):
        if barn[i] != None:
            continue
        if barn[i - 1] == div:
            curr = max(colors.iteritems(), key=operator.itemgetter(1))[0]
        else:
            for c in colors:
                if c != barn[i - 1]:
                    curr = c
        barn[i] = curr
        colors[curr] -= 1


    return "".join(barn)





def solve():
    N, R, O, Y, G, B, V = map(int, raw_input().split())
    assert R+O+Y+G+B+V == N
    return algorithm_small(N, R, O, Y, G, B, V)


T = int(raw_input())
for i in range(1, T + 1):
    ans = solve()
    print "Case #" + str(i) + ": " + str(ans)