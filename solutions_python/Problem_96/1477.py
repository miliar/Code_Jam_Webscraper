from collections import deque
import math


def main():
    with open('qual2.input', 'r') as f:
        for (i, line) in enumerate(f):
            if i is 0:
                continue
                #caseCount = line

            print 'Case #%s: %s' % (i, processCase(line))


def processCase(case):
    queue = deque(case.split())

    googlersCount = int(queue.popleft())
    surprisingCount = int(queue.popleft())
    bestResultMin = int(queue.popleft())
    positiveCount = 0

    scores = [int(i) for i in queue]
    scores.sort()
    for i in scores:
        (decomposed, wasSurprising) = decomposeScore(i, surprisingCount > 0)
        localMax = max(decomposed)
        if wasSurprising and localMax >= bestResultMin:
            surprisingCount = surprisingCount - 1

        #print i, localMax, '<=', bestResultMin, wasSurprising
        if localMax >= bestResultMin:
            positiveCount = positiveCount + 1

    return positiveCount


def decomposeScore(score, isSurprising):
    smaller = score / 3
    bigger = int(math.ceil(score / 3.0))
    wasSurprising = False

    out = list()
    out.append(bigger)

    if 2 * bigger + smaller is score:
        out.append(bigger)
    else:
        out.append(smaller)

    out.append(smaller)
    if score is not 0 and isSurprising and out[0] is out[1]:
        wasSurprising = True
        if out[1] is out[2]:
            out[0] = out[0] + 1
            out[2] = out[2] - 1
        else:
            out[0] = out[0] - 1
            out[1] = out[1] - 1
            out[2] = out[2] + 2

    return (out, wasSurprising)

if __name__ == "__main__":
    main()
