# 1, i, j, k

_1 = (1, 0, 0, 0)
minus_1 = (-1, 0, 0, 0)
i = (0, 1, 0, 0)
minus_i = (0, -1, 0, 0)
j = (0, 0, 1, 0)
minus_j = (0, 0, -1, 0)
k = (0, 0, 0, 1)
minus_k = (0, 0, 0, -1)

dic = {
        _1: {
            _1: _1,
            i: i,
            j: j,
            k: k,
            },
        minus_1: {
            _1: minus_1,
            i: minus_i,
            j: minus_j,
            k: minus_k,
            },
        i: {
            _1: i,
            i: minus_1,
            j: k,
            k: minus_j,
            },
        minus_i: {
            _1: minus_i,
            i: _1,
            j: minus_k,
            k: j,
            },
        j: {
            _1: j,
            i: minus_k,
            j: minus_1,
            k: i,
            },
        minus_j: {
            _1: minus_j,
            i: k,
            j: _1,
            k: minus_i,
            },
        k: {
            _1: k,
            i: j,
            j: minus_i,
            k: minus_1,
            },
        minus_k: {
            _1: minus_k,
            i: minus_j,
            j: i,
            k: _1,
            },
        }

def simplify(a, b):
    return dic[a][b]

def convert(a):
    if a == 'i':
        return i
    elif a == 'j':
        return j
    elif a == 'k':
        return k

def solve(info, line):
    length = int(info[0])
    repeat = int(info[1])

    count = 0
    current = _1

    has_i = False
    has_j = False

    while count < repeat:
        for m in xrange(len(line)):
            current = simplify(current, convert(line[m]))
            if not has_i:
                if current == i:
                    has_i = True
                    current = _1
            elif not has_j:
                if current == j:
                    has_j = True
                    current = _1
        count += 1
    return has_i and has_j and current == k

if __name__ == "__main__":
    testcases = input()

    for case in xrange(1, testcases+1):
        info = raw_input()
        line = raw_input()
        print("Case #%i: %s" % (case, 'YES' if solve(info.split(), line) else 'NO'))
