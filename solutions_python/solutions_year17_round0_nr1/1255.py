import sys


def main():
    sys.setrecursionlimit(10000)
    file = open('A-large.in', 'r')
    fileOut = open('output.txt', 'w')
    cases = int(file.readline())
    for x in range(cases):
        line = lineToList(file.readline())
        # print(line)
        answer = solve(line)
        if type(answer) is list:
            output = "Case #" + str(x + 1) + ": " + \
                str(' '.join(str(e) for e in answer))
        else:
            output = "Case #" + str(x + 1) + ": " + str(answer)
        # print(output)
        fileOut.write(output + '\n')
    file.close()
    fileOut.close()


def solve(line):
    steps = 0
    s = line[0]
    k = int(line[1])
    # print(k)
    if '-' in s:
        a = s.find('-')
        # print(a)
        steps = flip(s[a:], k, steps + 1)
    if steps is -1:
        steps = 'IMPOSSIBLE'
    return steps


def flip(s, k, steps):
    if len(s) < k:
        return -1
    # print(s)
    # print(k)
    n = ''
    for x in range(0, k):
        if s[x] is '-':
            n += '+'
        else:
            n += '-'
    n += s[k:]
    # print(n)
    if '-' in n:
        a = n.find('-')
        # print(a)
        steps = flip(n[a:], k, steps + 1)
    return steps


def lineToIntList(line):
    return map(int, line.strip().split())


def lineToList(line):
    return line.strip().split()


if __name__ == '__main__':
    main()
