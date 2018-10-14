from __future__ import division


def read(fname):
    '''
    return the input file line for line
    '''
    with open(fname, 'rb') as fid:
        data = fid.readlines()
    return data


def write(fname, case_list):
    with open(fname, 'wb') as fid:
        for i, case in enumerate(case_list):
            msg = 'Case #{}: {}\n'.format(i + 1, solve(case))
            fid.write(msg)


def parse(data):
    '''
    return a list of cases
    '''
    r, M = 1, []
    while r < len(data):
        case = data[r].strip()
        M.append(case)
        r += 1  # n
    return M


def f1(case):
    num = [int(i) for i in case]
    n = len(num)
    for i in range(n - 1):
        if num[i] > num[i + 1]:
            result = num[:i] + [num[i] - 1] + [9] * (n - i - 1)
            return str(int(''.join(str(k) for k in result)))
    return case


def f(case):
    case1 = f1(case)
    if case == case1:
        return case1
    return f(case1)


def solve(case):
    '''
    solve individual case
    return solution as string, or single scalar
    '''
    return f(case)


def main():
    infile = 'B-large.in.txt'
    outfile = 'out.txt'
    case_list = parse(read(infile))
    write(outfile, case_list)


if __name__ == '__main__':
    main()
