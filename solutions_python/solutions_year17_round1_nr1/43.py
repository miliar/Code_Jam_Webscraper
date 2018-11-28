# Python 3.5.2

from common import *

def extend(xs):
    n = len(xs)
    last = None
    count = 0
    answer = []
    for i in range(n):
        if xs[i] == '?':
            if last is None:
                count += 1
                continue
        else:
            last = xs[i]
        answer.append(last)

    if last is None:
        return ['?']
    else:
        return ([answer[0]] * count) + answer

def main(casenum):
    r, c = readints()
    xss = []
    for i in range(r):
        line = readline()
        xss.append(''.join(extend(line)))

    xss = extend(xss)

    writeline("Case #{}:".format(casenum))
    for xs in xss:
        writeline(xs)

run(main)
