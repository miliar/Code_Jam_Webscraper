t = int(raw_input())

for case in range(t):
    c, j = map(int, raw_input().split())
    ac = []
    aj = []
    for i in range(c):
        ac.append(map(int, raw_input().split()))
    for i in range(j):
        aj.append(map(int, raw_input().split()))
    ac = sorted(ac)
    aj = sorted(aj)
    if len(ac) + len(aj) == 1:
        print "Case #" + str(case + 1) + ": 2"
    elif len(ac) == 2:
        if ac[1][1] - ac[0][0] > 720 and ac[1][0] - ac[0][1] < 720:
            print "Case #" + str(case + 1) + ": 4"
        else:
            print "Case #" + str(case + 1) + ": 2"
    elif len(aj) == 2:
        if aj[1][1] - aj[0][0] > 720 and aj[1][0] - aj[0][1] < 720:
            print "Case #" + str(case + 1) + ": 4"
        else:
            print "Case #" + str(case + 1) + ": 2"
    else:
        print "Case #" + str(case + 1) + ": 2"
