def solve(R, C, B):
    ans = 0
    for cy in range(R):
        for cx in range(C):
            if B[cy][cx]!=".":
                ok = []
                for d in range(4):
                    x = cx
                    y = cy
                    while True:
                        x += [0,1,0,-1][d]
                        y += [-1,0,1,0][d]
                        if x<0 or C<=x or y<0 or R<=y:
                            f = False
                            break
                        if B[y][x]!='.':
                            f = True
                            break
                    ok += [f]
                if not any(ok):
                    return "IMPOSSIBLE"
                if not ok["^>v<".index(B[cy][cx])]:
                    ans += 1
    return ans

for t in range(input()):
    R,C = map(int, raw_input().split())
    B = [raw_input() for _ in range(R)]
    print "Case #%s: %s" % (t+1, solve(R,C,B))
