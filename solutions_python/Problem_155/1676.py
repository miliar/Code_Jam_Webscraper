

def solve(i, s_levels):
    levels = map(int, s_levels)

    s = 0
    need = 0
    for i, l in enumerate(levels):
        if i == 0:
            s += l
            continue

        if l != 0 and i > s:
            need += abs(i - s)
            s += l + abs(i - s)
        else:
            s += l

    return need


def main():
    inp_file = 'A-large.in'
    with open(inp_file, 'r') as f, open('output.txt', 'w') as f2:
        T = int(f.readline())
        for i in xrange(T):
            case = f.readline().strip()
            s_max, s_levels = case.split(' ')

            ans = solve(i+1, s_levels)
            ans_s = 'Case #{}: {}\n'.format(i+1, ans)
            f2.write(ans_s)

            # print s_max, s_levels
            # print ans_s


if __name__ == '__main__':
    main()
