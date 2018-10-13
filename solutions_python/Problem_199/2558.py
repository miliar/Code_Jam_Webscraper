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
        s, k = data[r].strip().split()
        M.append(([i for i in s], int(k)))
        r += 1  # n
    return M


def f(case):
    (s, k), n = case, 0
    for i in range(len(s) - k + 1):
        if not s[i] == '+':
            for j in range(k):
                s[i + j] = '+' if s[i + j] == '-' else '-'
            n += 1
    if not all(i == '+' for i in s):
        return 'IMPOSSIBLE'
    return str(n)


def solve(case):
    '''
    solve individual case
    return solution as string, or single scalar
    '''
    return f(case)


def main():
    infile = 'A-large.in.txt'
    outfile = 'out.txt'
    case_list = parse(read(infile))
    write(outfile, case_list)


if __name__ == '__main__':
    main()
