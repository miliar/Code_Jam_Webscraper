def read_input(path):
    with open(path, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()][1:]
        return lines


def solve(num):
    num = [int(d) for d in list(num)]
    for i in reversed(range(1, len(num))):
        if num[i] < num[i - 1]:
            num[i - 1] -= 1
            for j in range(i, len(num)):
                num[j] = 9
    return int(''.join(map(str, num)))

if __name__ == '__main__':
    cases = read_input('input.txt')
    for cn, case in enumerate(cases):
        out = solve(case)
        print('Case #{}: {}'.format(cn + 1, out))
