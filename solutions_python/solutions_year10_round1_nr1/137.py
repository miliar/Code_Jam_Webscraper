#!/opt/local/bin/python3.1
import sys

def find_row(table, length):
    res = []
    for ri in range(len(table)):
        for ci in range(len(table[ri])):
            # right
            for i in range(length):
                try:
                    if not table[ri][ci] == table[ri][ci + i]:
                        break
                except IndexError:
                    break
            else:
                res.append(table[ri][ci])
                res.append((ri, ci, 'right'))
                if res.count('R') and res.count('B'):
                    return 'Both'
            # right-down
            for i in range(length):
                try:
                    if not table[ri][ci] == table[ri + i][ci + i]:
                        break
                except IndexError:
                    break
            else:
                res.append(table[ri][ci])
                res.append((ri, ci, 'right-down'))
                if res.count('R') and res.count('B'):
                    return 'Both'
            # down
            for i in range(length):
                try:
                    if not table[ri][ci] == table[ri + i][ci]:
                        break
                except IndexError:
                    break
            else:
                res.append(table[ri][ci])
                res.append((ri, ci, 'down'))
                if res.count('R') and res.count('B'):
                    return 'Both'
            # left-down
            for i in range(length):
                if ci - i < 0:
                    break
                try:
                    if not table[ri][ci] == table[ri + i][ci - i]:
                        break
                except IndexError:
                    break
            else:
                res.append(table[ri][ci])
                res.append((ri, ci, 'left-down'))
                if res.count('R') and res.count('B'):
                    return 'Both'

    if res.count('R') and res.count('B'):
        return 'Both'
    elif res.count('R') and not res.count('B'):
        return 'Red'
    elif not res.count('R') and res.count('B'):
        return 'Blue'
    else:
        return 'Neither'

def rotate(table):
    result = []
    for row in range(len(table)):
        result.append([])
        for cell in table[row]:
            if not cell == '.':
                result[row].append(cell)
        result[row].reverse()
    return result

def main(argv=None):
    if not argv:
        argv = sys.argv

    infile = open(argv[1], 'r')
    outfile = open(argv[2], 'w')

    n_testcases = int(infile.readline())
    count = 0

    for line in infile:
        count += 1
        size, length = [int(n) for n in line.split()]
        table = []
        for i in range(size):
            table.append(infile.readline()[:-1])

        print('Case #{0}: {1}'.format(count, find_row(rotate(table), length)), file=outfile)

    if not n_testcases == count:
        print('{0} lines left. something wrong with the input file'.format(n_testcases - count))

if __name__ == '__main__':
    sys.exit(main())
