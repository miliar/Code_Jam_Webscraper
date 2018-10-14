def lawn(y, x, input):
    yh = [max(input[i]) for i in range(y)]
    xh = [max([input[i][j] for i in range(y)]) for j in range(x)]

    for i in range(y):
        for j in range(x):
            if input[i][j] < yh[i] and input[i][j] < xh[j]:
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    f = open('B-large.in')
    o = open('B-large.out', 'w')
    n = int(f.readline())
    for i in range(n):
        y, x = [int(c) for c in f.readline().split(' ')]
        input = []
        for j in range(y):
            input.append([int(c) for c in f.readline().split(' ')])
        o.write('Case #%d: %s\n'%(i+1, lawn(y, x, input)))
    o.close()
    f.close()
