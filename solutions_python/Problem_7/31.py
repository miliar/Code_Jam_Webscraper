import sys
import fileinput

def choose(n, k):
    if k < n:
        if k == 1:
            return n
        if k == 2:
            return n * (n - 1) / 2
        if k == 3:
            return n * (n - 1) * (n - 2) / 6
    return 0

def solve(T):
    T_m = map(lambda x: 3*(x[0]%3) + (x[1]%3), T)

    elems = {}
    for i in range(0, 9):
        elems[i] = 0

    for i in range(0, len(T_m)):
        elems[T_m[i]] += 1
    
    ret = 0
    for i in range(0, 9):
        for j in range(i+1, 9):
            for k in range(j+1, 9):
                x = int(i/3) + int(j/3) + int(k/3)
                y = (i%3) + (j%3) + (k%3)
                if (x%3) == 0 and (y%3) == 0:
#                    print "%d %d %d" % (elems[i], elems[j], elems[k])
                    ret += elems[i]*elems[j]*elems[k]

#    for i in range(0, 9):
#        for j in range(i+1, 9):
#            x = 2*(i/3) + j/3
#            y = 2*(i%3) + j%3
#            if x % 3 == 0 and y % 3 == 0:
#                ret = ret + choose(elems[i], 2)*elems[j]
#
#            x = i/3 + 2*(j/3)
#            y = i%3 + 2*(j%3)
#            if x % 3 == 0 and y % 3 == 0:
#                ret = ret + choose(elems[j], 2)*elems[i]

    for i in range(0, 9):
        ret += choose(elems[i], 3)

    return ret


if __name__ == '__main__':
    lines = fileinput.input(sys.argv[1])
    num = int(lines.readline())
    for i in range(1, num+1):
        (n, A, B, C, D, x_0, y_0, M) = map(int, lines.readline().split(' '))

        T = []

        T.append((x_0, y_0))

        X = x_0
        Y = y_0
        for j in range(1, n):
            X = ((A * X + B) % M)
            Y = ((C * Y + D) % M)
            T.append((X, Y))

        out = solve(T)

        print 'Case #%d: %d' % (i, out)


