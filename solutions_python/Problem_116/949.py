def rotate(data):
    assert len(data) is 4
    for d in data:
        assert len(d) is 4
    size = len(data)
    return [[data[size-1-i][j] for i in xrange(size)] for j in xrange(size)]

import re
pO = re.compile(r'[TO]'*4)
pX = re.compile(r'[TX]'*4)

def test():
    assert determine("XXTX") == (True, False, False)
    assert determine("OOOT") == (False, True, False)
    assert determine("XXX.") == (False, False, True)
    assert determine("TTTT") == (True, True, False)
    print "Passed"

def determine(row):
    row = ''.join(row)
    X, O, free = False, False, False
    if pO.search(row):
        O = True
    if pX.search(row):
        X = True
    if row.find('.') >= 0:
        free = True
    return X, O, free

def solve_0(data):
    X, O, free = False, False, False
    for row in data:
        x, o, f = determine(row)
        if x:
            X = True
        if o:
            O = True
        if f:
            free = True
    return X, O, free

def solve_1(data):
    X, O, free = False, False, False
    for i in xrange(len(data)):
        line = ''.join([data[i-j][j] for j in xrange(i+1)])
        x, o, f = determine(line)
        if x:
            X = True
        if o:
            O = True
        if f:
            free = True
    return X, O, free

def map_result(list):
    return (
        True in [l[0] for l in list],
        True in [l[1] for l in list],
        True in [l[2] for l in list]
        )

def solve(data):
    assert data == rotate(rotate(rotate(rotate(data))))
    l = [data]
    for i in xrange(3):
        data = rotate(data)
        l.append(data)
    result = [solve_1(r) for r in l]
    result.append(solve_0(data))
    result.append(solve_0(rotate(data)))
    assert map_result([(True, False, False), (False, False, True)]) == (True, False, True)
    X, O, free = map_result(result)
    #print X, O, free
    if not X and not O:
        if free:
            return "Game has not completed"
        else:
            return "Draw"
    if X and not O:
        return "X won"
    if O and not X:
        return "O won"
    raise "Error"


def main(f):
    T = int(f.readline().strip())
    for i in xrange(T):
        data = [list(f.readline().strip()) for r in range(4)]
        f.readline()
        print "Case #%d: %s" % (i+1, solve(data))

if __name__ == '__main__':
    #test()
    with open("A-large.in", 'r') as f:
        main(f)