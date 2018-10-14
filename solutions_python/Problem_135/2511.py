import itertools as it

from sys import argv

def _print(msg, f, stdout=True):
    f.write(msg + '\n')
    if stdout:
        print msg

extractRows = lambda raw: \
    map(int, raw[int(raw[0].rstrip())].rstrip().split())

if __name__ == '__main__':
    if len(argv) != 2:
        print 'Usage: {0} input-file'.format(argv[0])

    with open(argv[1], 'r') as f, \
           open(argv[1].rsplit('.')[0]+'.out', 'w') as o:
        N = int(f.readline())
        for case in xrange(N):
            case_str = 'Case #{0}: '.format(case+1)
            row1, row2 = (extractRows(list(it.islice(f, 5))),
                          extractRows(list(it.islice(f, 5))))
            intersection = list(set(row1) & set(row2))
            if len(intersection) == 0:
                _print(case_str + 'Volunteer cheated!', o)
            elif len(intersection) == 1:
                _print(case_str + '{0}'.format(intersection[0]), o)
            else:
                _print(case_str + 'Bad magician!', o)

