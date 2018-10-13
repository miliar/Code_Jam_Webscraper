def read_int():
    return int(raw_input())


def read_int_list():
    return [int(x) for x in raw_input().split()]


def solve():
    N = list(raw_input().strip())
    if N == ['0']:
        return '0'
    vals = list(reversed(N))
    for index in range(0, len(vals)-1):
        if vals[index] < vals[index + 1]:
            vals[index] = '9'
            for k in range(0, index):
                vals[k] = '9'
            b = int(vals[index + 1])
            if b - 1 >= 0:
                vals[index + 1] = str(b - 1)
    out = ''
    for v in reversed(vals):
        if v == '0' and out == '':
            continue
        out += v
    return out

def main():
    T = read_int()
    for i in range(T):
        print 'Case #%d: %s' % (i+1, solve())

if __name__ == '__main__':
    main()
