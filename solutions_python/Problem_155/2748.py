
'''
Problem A. Standing Ovation
'''


def read(fname):
    '''
    return the input file line for line
    '''
    with open(fname, 'rb') as fid:
        data = [line for line in fid.readlines()]
    return data


def write(fname, case_list, disp=False):
    with open(fname, 'wb') as fid:
        for i, case in enumerate(case_list):
            msg = 'Case #{0}: {1}\n'.format(i + 1, solve(case))
            if disp:
                print msg
            fid.write(msg)


def parse(data):
    '''
    return a list of cases
    '''
    r, M = 1, []
    while r < len(data):
        case = [int(x) for x in data[r].split()[1]]
        M.append(case)
        r += 1  # n
    return M


def solve(case):
    '''
    solve individual case
    return solution as string
    '''
    i, cumsum, addition = 1, case[0], 0
    while i < len(case):
        if cumsum < i:
            d = i - cumsum
            cumsum += d
            addition += d
        cumsum += case[i]
        i += 1
    return str(addition)


def main():
    infile = 'A-large.in'
    outfile = 'A-large_out.txt'
    case_list = parse(read(infile))
    write(outfile, case_list)

if __name__ == '__main__':
    main()
