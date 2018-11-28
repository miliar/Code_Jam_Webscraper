def getRegularScore(n):
    b = n / 3
    if n % 3 > 0:
        return b+1
    else:
        return b

def getSuprisingScore(n):
    b = n / 3
    if n % 3 == 2:
        return b+2
    else:
        return b+1

def find(scores, nSuprises, p):
    count = 0
    for s in scores:
        rs = getRegularScore(s)
        if rs >= p:
            count += 1
        elif s > 1 and nSuprises > 0:
            ss = getSuprisingScore(s)
            if ss >= p:
                count += 1
                nSuprises -= 1
    return count

def solve(f = None):
    answers = []
    if f != None:
        handle = open(f)
    else:
        handle = sys.stdin
    n = int(handle.readline())
    for i in xrange(n):
        array = [int(s) for s in handle.readline().strip().split(" ")]
        answers.append(find(array[3:], array[1], array[2]))
    for i in xrange(n):
        print "Case #%d: %s" % (i+1, answers[i])
