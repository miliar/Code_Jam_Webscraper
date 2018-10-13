def solve(X, S, R, t, N, walkways):
    #print(X, S, R, t, N, walkways)
    steps = []
    walkways.append((X, X, S))
    d = walkways[0][0]
    for i in range(N):
        d += walkways[i + 1][0] - walkways[i][1]
        steps.append((S + walkways[i][2], walkways[i][1] - walkways[i][0]))
    steps.append((S, d))
    steps.sort()
    r = R - S
    time = 0
    for v, d in steps:
        run = min(d, t * (v + r))
        walk = d - run
        time += run / (v + r) + walk / v 
        t -= run / (v + r)
    return time

def main():
    T = int(input())
    for i in range(1, T + 1):
        X, S, R, t, N = map(int, input().split())
        walkways = [tuple(map(int, input().split())) for j in range(N)]
        ans = solve(X, S, R, t, N, walkways)
        print('Case #%d: %.6f' % (i, ans))

if __name__ == '__main__':
    main()

