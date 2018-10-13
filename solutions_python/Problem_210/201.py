
t = int(raw_input())

for case in range(t):

    c, d = [int(s) for s in raw_input().split()]
    opt = []
    for i in range(c):
        opt.append([int(s) for s in raw_input().split()])
    for j in range(d):
        opt.append([int(s) for s in raw_input().split()])

    ans = 0

    if c + d == 1:
        ans = 2
    elif c == 1 and d == 1:
        ans = 2
    else:
        opt.sort(key=lambda x: x[0])
        if opt[1][1] - opt[0][0] <= 720 or opt[0][1] - opt[1][0] + 1440 <= 720:
            ans = 2
        else:
            ans = 4

    print "Case #%d: %d" % (case + 1, ans)