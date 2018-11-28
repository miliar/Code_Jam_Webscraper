import sys

def get_max_tidy_number(n):
    digits = [int(d) for d in list(str(n))]
    if len(digits) == 1:
        return n
    up = -1
    for i in range(0, len(digits) - 1):
        if digits[i] > digits[i + 1]:
            break
        up += 1
    if up == len(digits) - 2:
        return n
    order = pow(10, len(digits) - up - 2)
    return get_max_tidy_number(n / order * order - 1)

if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open(sys.argv[1])]
    t = int(lines[0])
    for i in range (1, t + 1):
        res = get_max_tidy_number(long(lines[i]))
        print('Case #%d: %ld' % (i, res))
