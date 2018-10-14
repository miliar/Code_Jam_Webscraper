import sys

def next_line():
    return input_file.readline().rstrip()

input_file = open(sys.argv[1])
for case in range(1, int(next_line())+1):
    print "Case #%s:" % (case),
    N = map(int, next_line())
    last = 0
    res = []
    equal_start = 0
    for i, c in enumerate(N):
        if i == 0:
            continue
        if c > N[i-1]:
            res.extend(N[equal_start:i])
            equal_start = i
        elif c < N[i-1]:
            res.append(N[equal_start] - 1)
            for j in xrange(equal_start+1, len(N)):
                res.append(9)
            break
    else:
        res.extend(N[equal_start:])
    print int("".join(map(str, res)))

