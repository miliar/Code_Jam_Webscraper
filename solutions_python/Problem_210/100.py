import sys


def count_exchanges(time_table):
    cp = time_table[0]
    ex = 0
    for p in time_table:
        if p != cp:
            cp = p
            ex += 1
    if time_table[0] != time_table[-1]:
        ex += 1
    return ex


def solve_case(time_table, cares, case_number):
    cares.sort(key=lambda c: c[0])
    rest = {'c': 720 - time_table.count('c'), 'j': 720 - time_table.count('j')}

    can_cares = []
    for idx, care in enumerate(cares):
        pcare = cares[idx - 1]
        if care[2] == pcare[2]:
            t = care[0] - pcare[1]
            if t < 0:
                t = 1440 + t
            can_cares.append((t, pcare[1], care[0], care[2]))

    can_cares.sort(key=lambda c: c[0])
    for can_care in can_cares:
        if rest[can_care[3]] >= can_care[0]:
            if can_care[1] > can_care[2]:
                time_table[:can_care[2]] = [can_care[3]] * can_care[2]
                time_table[can_care[1]:] = [can_care[3]] * (1440 - can_care[1])
            else:
                time_table[can_care[1]:can_care[2]] = [can_care[3]] * (can_care[2] - can_care[1])
            rest[can_care[3]] -= can_care[0]

    while time_table[0] == '':
        t = time_table.pop(0)
        time_table.append(t)

    lp = rest['c']
    for t in range(0, 1440):
        if time_table[t] != '':
            lp = time_table[t]
            continue
        if lp == 'c':
            if rest[lp] > 0:
                time_table[t] = 'c'
            else:
                lp = 'j'
                time_table[t] = 'j'
        else:
            if rest[lp] > 0:
                time_table[t] = 'j'
            else:
                lp = 'c'
                time_table[t] = 'c'
        rest[lp] -= 1
    print("Case #%d: %d" % (case_number, count_exchanges(time_table)))


def main():
    f = sys.stdin
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')

    total_cases = f.readline()
    for case_number in range(1, int(total_cases) + 1):
        c, j = map(int, f.readline().strip().split(' '))
        time_table = [''] * 1440
        cares = []
        for _ in range(0, c):
            s, e = map(int, f.readline().strip().split(' '))
            time_table[s:e] = ['j'] * (e - s)
            cares.append((s, e, 'j'))
        for _ in range(0, j):
            s, e = map(int, f.readline().strip().split(' '))
            time_table[s:e] = ['c'] * (e - s)
            cares.append((s, e, 'c'))

        solve_case(time_table, cares, case_number)


if __name__ == "__main__":
    main()
