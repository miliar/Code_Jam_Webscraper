__author__ = 'PavelM'





def solve():
    c, f, x = map(float, in_file.readline().split())
    r = 2.0
    t = 0
    while True:
        if c >= x:
            return x / r

        t += c/r

        t1 = (x - c)/ r
        t2 = x / (r + f)

        if t1 <= t2:
            return t + t1
        r += f



if __name__ == '__main__':
    with open('B-large.out', 'w') as output:
        with open('B-large.in') as in_file:
            n = int(in_file.readline())
            for k in range(1, n+1):
                output.write('Case #{0}: {1}\n'.format(k, solve()))