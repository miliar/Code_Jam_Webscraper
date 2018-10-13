f = open('B-large.in','r')
text = f.read()
text = text.replace('\r','').strip()
lines = text.split('\n')
count = lines[0]
cases = lines[1:]
caseIdx = 1

for i in xrange(int(count)):
    tokens = cases[i].strip().split(' ')
    C = float(tokens[0])
    F = float(tokens[1])
    X = float(tokens[2])

    current = 2

    t = 0

    if C >= X:
        t = X/2.0
    else:
        while True:
            currentFinal = X/current
            farmTime = C/current
            nextFinal = X/(current+F)
            if currentFinal < farmTime+nextFinal:
                t += currentFinal
                break;
            else:
                current += F
                t += farmTime

    print 'Case #'+str(caseIdx)+': '+str(t)
    caseIdx += 1

