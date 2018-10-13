__author__ = 'PavelM'




def solve():
    a, b, k = (int(i) for i in in_file.readline().split())
    c = 0
    for a1 in range(a):
        for b1 in range(b):
            if a1&b1 < k:
                c += 1
    return c




if __name__ == '__main__':
    name = 'B-small-attempt0'
    with open('%s.out' % name, 'w') as output:
        with open('%s.in' % name) as in_file:
            n = int(in_file.readline())
            for k in range(1, n + 1):
                output.write('Case #{0}: {1}\n'.format(k, solve()))