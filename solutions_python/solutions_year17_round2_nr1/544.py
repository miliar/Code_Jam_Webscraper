t = int(input())
for i in range(t):
    d, n = map(int, input().split())
    horses = []
    for j in range(n):
        horses.append(list(map(int, input().split())))
    min_sp = -1
    for j in range(n):
        dur = (d - horses[j][0]) / horses[j][1]
        sp = d / dur
        if min_sp == -1 or sp < min_sp:
            min_sp = sp
    print('Case #%d: %.6f' % (i + 1, min_sp))
