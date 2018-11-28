import sys

def chance(prob, typed):
    chances = []
    for t in range(2**typed):
        pp = []
        for p in zip(prob, bin(t)[2:].zfill(len(prob))):
            if p[1] == '0':
                pp.append(p[0])
            else:
                pp.append(1.0 - p[0])
        chances.append(reduce(lambda x, y: x*y, pp))
    return chances
        

def kt(length, typed, pp):
    correct = float(length-typed+1)
    incorrect = correct + float(length) + 1.0
    strokes = [correct*pp[0]]
    strokes += [incorrect*p for p in pp[1:]]
    return sum(strokes)

def bs1(length, typed, pp):
    if typed < 1:
        return 2 + length
    correct = float(3 + length - typed)
    incorrect = correct + float(length) + 1.0
    strokes = [correct*p for p in pp[:2]]
    strokes += [incorrect*p for p in pp[2:]]
    return sum(strokes)
    
def bs2(length, typed, pp):
    if typed < 3:
        return 3 + length
    correct = float(5 + length - typed)
    incorrect = float(correct + length + 1)
    strokes = [correct*p for p in pp[:4]]
    strokes += [incorrect*p for p in pp[4:]]
    return sum(strokes)
    
def enter_now(length, typed, prob):
    return length + 2
    
def num_strokes(length, typed, prob):
    pp = chance(prob, typed)
    strokes = [enter_now(length, typed, pp), bs2(length, typed, pp), 
        bs1(length, typed, pp), kt(length, typed, pp)]
    return min(strokes)

if __name__ == '__main__':
    testcases = int(sys.stdin.readline())
    for i in range(testcases):
        t, l = map(int, sys.stdin.readline().split())
        p = map(float, sys.stdin.readline().split())
        print "Case #{}: {:f}".format(i+1, num_strokes(l, t, p))
    sys.exit()

