import os
from copy import deepcopy


def reader(file):
    f_out = file[:-2] + "out"
    if os.path.isfile(f_out):
        with open(f_out, 'w') as f:  # clear the output file
            f.write('')
    with open(file, 'r') as f:
        T = int(f.readline())
        for t in range(T):
            r, c = map(int, f.readline().split(' '))
            case = [[letter for letter in f.readline().strip()] for _ in range(r)]
            solver(t, r, c, case, f_out)


def solver(t, r, c, case, f_out):
    print("Solving case #{}.".format(t + 1))
    print("Parameters R: {}, C: {}.".format(r, c))
    cake = solve_case(r, c, case)
    with open(f_out, 'a') as f:
        f.write("Case #{}:\n".format(t + 1))
        for row in cake:
            f.write("{}\n".format(''.join(row)))
    print("Case #{} solved.".format(t + 1))
    print('*' * 10)


def solve_case(r, c, case):
    cake = deepcopy(case)
    for i, row in enumerate(cake):
        n = row.count('?')
        if n == c:
            continue
        _row = handle_row(row)
        r_row = _row[::-1]
        r_row_s = handle_row(r_row)
        cake[i] = r_row_s[::-1]
    cake = handle_q_m_row(cake)
    cake = handle_q_m_row(cake[::-1])
    return cake[::-1]


def handle_row(row):
    for q_i, q in enumerate(row):
        if q == '?':
            if q_i != 0:
                row[q_i] = row[q_i - 1]
        else:
            continue
    return row


def handle_q_m_row(cake):
    for r_i, r in enumerate(cake):
        if '?' in r:
            if r_i != 0:
                cake[r_i] = cake[r_i - 1]
        else:
            continue
    return cake


def main():
    import time
    a = time.time()
    reader('A-large.in')
    b = time.time()
    print("Cases solved in {}s.".format(b-a))
    # with open('A-large.in', 'w') as f:  # clear the output file
    #     f.write('100\n')
    #     for _ in range(100):
    #         f.write('25 25\n')
    #         f.write('?'*24 + 'A\n')
    #         for k in range(24):
    #             f.write('?'*25 + '\n')

main()
