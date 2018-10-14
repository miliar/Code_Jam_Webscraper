T = int(raw_input())
for t in range(0, T):
    AC, AJ = map(int, raw_input().split(' '))
    C = []
    D = []
    J = []
    K = []
    C = []
    J = []
    for i in range(0, AC):
        c, d = map(int, raw_input().split(' '))
        C.append((c, d))
    for i in range(0, AJ):
        j, k = map(int, raw_input().split(' '))
        J.append((j, k))
    C.sort(key=lambda x: x[0])
    J.sort(key=lambda x: x[0])
    if AC == 0:
        if AJ == 1:
            print "Case #" + str(t+1) + ": " + str(2)
            continue
        if J[1][1] - J[0][0] <= 720:
            print "Case #" + str(t+1) + ": " + str(2)
            continue
        elif 1440 - J[1][0] + J[0][1] <= 720:
            print "Case #" + str(t+1) + ": " + str(2)
            continue
        else:
            print "Case #" + str(t+1) + ": " + str(4)
            continue
    if AJ == 0:
        if AC == 1:
            print "Case #" + str(t+1) + ": " + str(2)
            continue
        if C[1][1] - C[0][0] <= 720:
            print "Case #" + str(t+1) + ": " + str(2)
            continue
        elif 1440 - C[1][0] + C[0][1] <= 720:
            print "Case #" + str(t+1) + ": " + str(2)
            continue
        else:
            print "Case #" + str(t+1) + ": " + str(4)
            continue
    print "Case #" + str(t+1) + ": " + str(2)

