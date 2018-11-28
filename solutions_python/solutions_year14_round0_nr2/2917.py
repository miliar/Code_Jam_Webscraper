f = open('C:/Users/rob/Downloads/b-large.in', 'r')
T = int(f.readline())

for n in range(T):
    C, Rf, X = (float(x) for x in f.readline().split())

    r = 2
    t = 0
    while True:
        finishT = X/r
        buildT = C/r + X/(r+Rf)

        if buildT > finishT:
            print('Case #' + str(1+n) + ': ' + str(t + finishT))
            break
        else:
            t += C/r
            r += Rf