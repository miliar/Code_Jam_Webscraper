import sys


def solve(line, test_case):
    
    l = len(line)
    digits = [int(x) for x in line]
    
    pos = None
    for i in range(1, l):
        if digits[i] < digits[i - 1]:
            pos = i
            break
    
    if pos is None:
        num = line
    else:
        num = '9' * (l - pos)
        decr = 1
        for i in range(pos - 1, -1, -1):
            d = digits[i] - decr
            if (i > 0) and (d < digits[i-1]):
                d = 9
                decr = 1
            else:
                if d == 0:
                    break
                decr = 0
            num = str(d) + num
    
    print('Case #{}: {}'.format(test_case, num))


def solve_all(input_file):
    
    with open(input_file) as f:
        for t, l in enumerate(f):
            if (t > 0) and (l.strip() != ''):
                solve(l.strip(), t)


if __name__ == '__main__':
    solve_all(sys.argv[1])