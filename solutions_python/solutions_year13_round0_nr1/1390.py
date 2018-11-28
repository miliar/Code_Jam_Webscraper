import sys
data = []

def hor(data):
    for x in data:
        yield x

def ver(data):
    for x in range(4):
        yield [y[x] for y in data]

def diag(data):
    yield data[0][0], data[1][1] , data[2][2] , data[3][3]
    yield data[0][3], data[1][2] , data[2][1] , data[3][0]

def test(s, flag=False):
    print 'test |%s|' % str(s)
    loc = '.' in s
    if not loc and not 'O' in s:
        raise Exception('X won')
    if not loc and not 'X' in s:
        raise Exception('O won')
    return flag or loc

def play(handle):
    data = [handle.readline()[:4] for x in range(4)]
    print 'data', data
    handle.readline()
    flag = False
    try:
        for d in hor(data):
            flag = test(d, flag)
        for d in ver(data):
            flag = test(d, flag)
        d = data
        flag = test(''.join([d[0][0], d[1][1] , d[2][2] , d[3][3]]), flag)
        flag = test(''.join([d[0][3], d[1][2] , d[2][1] , d[3][0]]), flag)
    except Exception as e:
        return str(e)
    if flag:
        return 'Game has not completed'
    return 'Draw'

def main():
    with open(sys.argv[1]) as handle:
        count = int(handle.readline())
        print count
        result = ['Case #%s: %s' % (i + 1, play(handle)) for i in range(count)]
        with open(sys.argv[1][:-2] + 'out', 'w') as h:
            h.write('\n'.join(result))

main()
