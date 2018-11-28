title = 'B'
scale = 'large'

fpout = open(title + '-' + scale + '.out', 'w')
def presult(casenum, s):
    fpout.write('Case #' + str(casenum) + ': ' + s + '\n')



f = open(title + '-' + scale + '.in', 'r')


num_case = int(f.readline().rstrip())

for casen in range(1, num_case+1):
    C, F, X = [float(x) for x in f.readline().rstrip().split()]
    print(C, F, X)
    if C > X:
        presult(casen, str(X/2.0))
        continue
    currentRate = 2.0
    ctime = 0.0
    while True:
        ctime += C / currentRate
        nobuytime = (X-C) / currentRate
        buytime = X / (currentRate + F)
        if nobuytime <= buytime:
            print('nobuy')
            ctime += nobuytime
            break
        else:
            print('buy')
            currentRate += F
            continue
    presult(casen, "%.8f" % (ctime,))
        


