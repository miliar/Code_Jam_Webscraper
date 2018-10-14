# Joseph Lee <gengarkhan@gmail.com>
#

def test_case(case):
    field = map(lambda r: map(int, r.strip().split(' ')), case)

    valid_col = []
    for c in xrange(len(field[0])):
        col = map(lambda x: x[c], field)
        if len(set(col)) > 1:
            valid_col.append(False)
        else:
            valid_col.append(True)
    if False not in valid_col:
        return 'YES'
    
    for row in field:
        shorter = sorted(set(row))[:-1]
        # uniform row
        if not shorter:
            continue
        for i in xrange(len(row)):
            # check if column is valid
            if row[i] in shorter:
                # check validity of column i
                if valid_col[i]:
                    continue
                else:
                    return 'NO'
    return 'YES'


def main(arg):
    fname = arg
    with open(fname, 'r') as infile:
        lines = infile.readlines()
    t = lines.pop(0)

    count = 1
    while len(lines) > 0:
        n, m = map(int, lines.pop(0).strip().split(' '))
        case, lines = lines[0:n], lines[n:]
        print 'Case #%d: %s' % (count, test_case(case))
        count += 1



if __name__ == '__main__':
    from sys import argv
    main(argv[1])
