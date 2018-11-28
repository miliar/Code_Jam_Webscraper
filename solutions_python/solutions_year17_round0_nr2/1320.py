import sys


def main():
    sys.setrecursionlimit(10000)
    file = open('B-large.in', 'r')
    fileOut = open('output.txt', 'w')
    cases = int(file.readline())
    for x in range(cases):
        line = lineToIntList(file.readline())
        print(line)
        answer = solve(line[0])
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
    s = str(line)
    e = len(s) - 1
    ans = ''
    if len(s) is 1:
        return s
    rerun = False
    for x in range(0, e):
        c = int(s[x:x + 1])
        n = int(s[x + 1:x + 2])
        if n < c:
            c = c - 1
            ans = str(ans) + str(c)
            ans += ('9' * (len(s) - x - 1))
            rerun = True
            break
        else:
            ans = str(ans) + str(c)
            if x is e - 1:
                ans += str(n)
    # print(ans)
    if rerun:
        ans = solve(ans)
    return int(ans)


def lineToIntList(line):
    return map(int, line.strip().split())


def lineToList(line):
    return line.strip().split()


if __name__ == '__main__':
    main()
