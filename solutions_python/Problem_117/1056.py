import sys

INPUT_FILE_INDEX = 1

def solve(rows_count, cols_count, lines):
    #print '\n\n[D] === Test case: ===== \n%d %d\n%s\n--------\n' % \
    #        (rows_count, cols_count, '\n'.join([str(i) for i in lines]))
    
    rows = lines
    cols = zip(*lines)
    row_max = [max(row) for row in rows]
    col_max = [max(col) for col in cols]

    for row in xrange(rows_count):
        for col in xrange(cols_count):
            num = lines[row][col]
            if num < row_max[row] and num < col_max[col]:
                #print (row, col, num, row_max[row], col_max[col])
                #print '[FAILURE BECAUSE:] row: %d col: %d num: %d, row_max: %d, col_max: %d' % (row, col, num, row_max[row], col_max[col])
                return 'NO'

    return 'YES'

def line_gen(input_path):
    with open(input_path) as input:
        while True:
            yield input.readline()

def get_next_input(lines):
    rows, cols = map(int, lines.next().split())
    return (rows, cols, [map(int, lines.next().strip().split()) for i in xrange(rows)])

def main():
    lines = line_gen(sys.argv[INPUT_FILE_INDEX])
    test_cases = int(lines.next())

    for t in xrange(1, test_cases + 1):
        case_input = get_next_input(lines)
        print 'Case #{0}: {1}\n'.format(t, solve(*case_input)),
        
if '__main__' == __name__:
    main()
