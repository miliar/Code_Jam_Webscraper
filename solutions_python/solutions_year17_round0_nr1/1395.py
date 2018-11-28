import sys

HAPPY_SIDE = '+'
DARK_SIDE = '-'

def read_data(filename):
    with open(filename) as f:
        cases = int(f.readline().strip())
        data = []
        for i in xrange(cases):
            row, K = f.readline().strip().split()
            data.append({'row': list(row), 'K': int(K)})
        return data

def flip_pancakes(data):
    case_num = 1
    for case in data:
        movements = 0
        row = case['row']
        K = case['K']
        # print 'Row: {}'.format(''.join(row))
        for i in range(len(row) - (K - 1)):
            if row[i] == DARK_SIDE:
                movements += 1
                row[i] = HAPPY_SIDE
                for offset in range(1, K):
                    row[i + offset] = HAPPY_SIDE if row[i + offset] == DARK_SIDE else DARK_SIDE
                # print 'Row: {}'.format(''.join(row))
        movements = movements if all(_ == HAPPY_SIDE for _ in row) else 'IMPOSSIBLE'
        print "Case #{}: {}".format(case_num, movements)
        case_num += 1


if __name__ == '__main__':
    file_name = sys.argv[1]

    flip_pancakes(read_data(file_name))
