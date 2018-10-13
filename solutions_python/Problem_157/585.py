__author__ = 'Dmytro'

infile = open('C-small-attempt2.in')
outfile = open('out.txt', 'w')

m_table = {
    ' ': {' ': (1, ' '), 'i': ( 1, 'i'), 'j': ( 1, 'j'), 'k': ( 1, 'k')},
    'i': {' ': (1, 'i'), 'i': (-1, ' '), 'j': ( 1, 'k'), 'k': (-1, 'j')},
    'j': {' ': (1, 'j'), 'i': (-1, 'k'), 'j': (-1, ' '), 'k': ( 1, 'i')},
    'k': {' ': (1, 'k'), 'i': ( 1, 'j'), 'j': (-1, 'i'), 'k': (-1, ' ')}
}

def mult(a, b):
    global m_table
    (sign, value) = m_table[a[1]][b[1]]
    return sign * a[0] * b[0], value

def check_all(precomp, big_string):
    m1 = (1, ' ')
    for index1 in xrange(N):
        m1 = mult(m1, (1, big_string[index1]))
        if m1 == (1, 'i'):
            m2 = (1, ' ')
            for index2 in xrange(index1 + 1, N):
                m2 = mult(m2, (1, big_string[index2]))
                if m2 == (1, 'j') and index2 + 1 < len(big_string) and precomp[index2 + 1] == (1, 'k'):
                    return 'YES'
    return 'NO'

T = int(infile.readline())
for t in xrange(1, T + 1):
    values = infile.readline().split(' ')
    L = int(values[0])
    X = int(values[1])
    pattern = infile.readline()
    pattern = pattern.rstrip()

    N = X * L

    result = "NO"
    if L > 1:
        big_string = ''.join([pattern for x in xrange(X)])
        precomp = [(1, ' ') for x in xrange(N)]

        precomp[-1] = (1, big_string[-1])
        for index1 in xrange(1, N, 1):
            precomp[N - 1 - index1] = mult((1, big_string[N - index1 - 1]), precomp[N - index1])
        result = check_all(precomp, big_string)


    outfile.write("Case #{0}: {1}\n".format(t, result))
    print 'test', t








