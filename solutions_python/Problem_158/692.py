mem = [[],
       [1,2,3,4,5,6,7,8,9,10],
       [2,4,5,6,7,9,10],
       [6,8,9],
       [9,10]]
T = int(raw_input())

for t in range(1, T + 1):
    x, r, c = map(int, raw_input().split())
    if r > c:
        r, c = c, r
    if r == 1:
        case = c
    elif r == 2:
        case = 5 + c - 2
    elif r == 3:
        case = 8 + c - 3
    elif r == 4:
        case = 10
    answer = "GABRIEL" if case in mem[x] else "RICHARD"
    print "Case #%d: %s" % (t, answer)
