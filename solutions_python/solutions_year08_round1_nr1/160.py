import sys
import psyco

def solve(x, y):
    x.sort()
    y.sort()
    out = 0
    count = 0
    for i in x:
        if i < 0:
            out += i * y.pop(-1)
            count += 1
        else:
            break
    x = x[count:]
    count = 0
    for i in y:
        if i < 0:
            out += i * x.pop(-1)
            count += 1
        else:
            break
    y = y[count:]
    y.reverse()
    out += sum(map(lambda x, y: x*y, x,y))

    return out


def main():
    file = open(sys.argv[1], 'r')
    nc = int(file.readline())

    count = 1
    for case in range(nc):
        T = int(file.readline())
        x = [int(i) for i in file.readline().split()]
        y = [int(i) for i in file.readline().split()]
        out = solve(x,y)


        print 'Case #' + str(count) + ':', out
        count += 1

if __name__ == "__main__":
    #g = psyco.proxy(main)
    #g()
    main()
