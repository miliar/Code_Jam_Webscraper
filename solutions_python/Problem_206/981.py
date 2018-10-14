def parse():
    d, n = map(int, input().split())
    horses = []
    for _ in range(n):
        horses.append(tuple(map(int, input().split())))
    return d, n, horses

def time_til_dest(d, h):
    k, s = h[0], h[1]
    time = (d - k)/s
    return time

def solve(d, n, horses):
    time = max([time_til_dest(d, h) for h in horses])
    ans = d / time
    print('{0:.6f}'.format(ans))

t = int(input())
for tc in range(t):
    print("Case #" + str(tc + 1) + ":", end=' ')
    solve(*parse())
