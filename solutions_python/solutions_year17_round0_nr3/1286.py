import sys
import math


def main():
    sys.setrecursionlimit(10000)
    file = open('C-small-2-attempt0.in', 'r')
    fileOut = open('output.txt', 'w')
    cases = int(file.readline())
    for x in range(cases):
        line = lineToIntList(file.readline())
        print(line)
        answer = solve(line)
        if type(answer) is list:
            output = "Case #" + str(x + 1) + ": " + \
                str(' '.join(str(e) for e in answer))
        else:
            output = "Case #" + str(x + 1) + ": " + str(answer)
        print(output)
        fileOut.write(output + '\n')
    file.close()
    fileOut.close()


def solve(line):
    n = line[0]
    # print(n)
    k = line[1]
    # print(k)
    p = int(math.log2(k))
    # print(p)
    mx = int((n - k + 2**p) / (2**(p + 1)))
    mn = int((n - k) / (2**(p + 1)))
    # print(mx)
    # print(mn)
    return [mx, mn]


def lineToIntList(line):
    return list(map(int, line.strip().split()))


def lineToList(line):
    return line.strip().split()


if __name__ == '__main__':
    main()
