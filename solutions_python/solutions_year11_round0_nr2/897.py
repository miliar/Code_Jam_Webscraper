#!/usr/bin/python

import sys

def solve(combined, opposed, invoked):
    cmap = {}
    omap = {}

    for c in combined:
        if c[0] not in cmap: cmap[c[0]] = {}
        if c[1] not in cmap: cmap[c[1]] = {}
        cmap[c[0]][c[1]] = cmap[c[1]][c[0]] = c[2]

    for o in opposed:
        if o[0] not in omap: omap[o[0]] = set()
        if o[1] not in omap: omap[o[1]] = set()
        omap[o[0]].add(o[1])
        omap[o[1]].add(o[0])

    result = []

    for elem in invoked:
        if len(result) == 0:
            result.append(elem)

        elif elem in cmap and result[-1] in cmap[elem]:
            t = result.pop()
            result.append(cmap[elem][t])

        elif elem in omap:
            for o in omap[elem]:
                if o in result:
                    result = []
                    break
            else:
                result.append(elem)

        else:
            result.append(elem)

    return result

def main():
    t = int(sys.stdin.readline())

    for i in range(t):
        line = sys.stdin.readline().strip().split()

        c, d, n = map(int, filter(lambda x : x.isdigit(), line))

        print 'Case #%d: [%s]' % (i+1, ", ".join(solve(line[1:1+c], line[2+c:2+c+d], line[-1])))


if __name__ == '__main__':
    main()
