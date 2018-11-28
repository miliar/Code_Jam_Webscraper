import sys

# sys.stdin = open('a.in', 'r')
# sys.stdin = open('A-small-attempt0.in', 'r')
# sys.stdout = open('A-small-attempt0.out', 'w')
sys.stdin = open('A-large.in', 'r')
sys.stdout = open('A-large.out', 'w')

for t in range(int(input())):

    R, C = list(map(int, input().split()))

    G = [input() for r in range(R)]

    # print(G)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    D = {
        'v': 0,
        '>': 1,
        '^': 2,
        '<': 3,
        '.': -1,
    }

    result = 0

    def inside(rr, cc):
        return 0 <= rr < R and 0 <= cc < C

    def safe(rr, cc, d):
        while True:
            rr += dx[d]
            cc += dy[d]
            if not inside(rr, cc):
                return False
            elif G[rr][cc] == '.':
                continue
            else:
                return True
        return False

    for r in range(R):
        for c in range(C):

            # print('RC:', r, c, D[G[r][c]], 'safe:', safe(r, c, D[G[r][c]]))

            if result == 'IMPOSSIBLE':
                continue
            rr, cc = r, c
            d = D[G[r][c]]
            if G[rr][cc] == '.' or safe(rr, cc, d):
                continue
            found = False
            for dd in range(4):
                if dd == d:
                    continue
                if safe(rr, cc, dd):
                    found = True
            if not found:
                result = 'IMPOSSIBLE'
                break
            else:
                result += 1

    print('Case #%d: %s' % (t + 1, result))

sys.stdin.close()
sys.stdout.close()