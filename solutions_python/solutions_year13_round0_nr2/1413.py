filename = 'B-large'
f_in = open(filename + '.in')
f_out = open(filename + '.out', 'w')

count = int(f_in.readline())


def check(lawn, i, j):
    n_max = {}
    m_max = {}

    for n in xrange(i):
        for m in xrange(j):
            if n not in n_max or lawn[n][m] > n_max[n]:
                n_max[n] = lawn[n][m]

            if m not in m_max or lawn[n][m] > m_max[m]:
                m_max[m] = lawn[n][m]

    print('n_max: ' + str(n_max))
    print('m_max: ' + str(m_max))

    for n in xrange(i):
        for m in xrange(j):
            '''
            a = b = l = r = False

            if n == 0:
                a = True
            if n > 0 and lawn[n-1][m] <= lawn[n][m]:
                a = True
            if n == (i - 1):
                b = True
            if n < (i - 1) and lawn[n+1][m] <= lawn[n][m]:
                b = True
            if m == 0:
                l = True
            if m > 0 and lawn[n][m-1] <= lawn[n][m]:
                l = True
            if m == (j - 1):
                r = True
            if m < (j - 1) and lawn[n][m+1] <= lawn[n][m]:
                r = True

            if (a and b) or (l and r):
                continue
            '''

            if lawn[n][m] < n_max[n] and lawn[n][m] < m_max[m]:
                print('%d, %d fail' % (n, m))
                
                return 'NO'

    return 'YES'


for case in xrange(1, count + 1):
    dim = map(int, f_in.readline().split(' '))

    lawn = {}

    for n in xrange(dim[0]):
        lawn[n] = map(int, f_in.readline().strip().split(' '))

    r = check(lawn, dim[0], dim[1])
            
    print('Case #%d: %s\n' % (case, r))
    f_out.write('Case #%d: %s\n' % (case, r))
