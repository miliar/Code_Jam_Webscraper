#!/usr/bin/python3
from sys import argv

def main(args):
    with open(args[1]) as inp, open(args[2], 'w') as out:
        cases = int(inp.readline())
        for case in range(0, cases):
            blocks = int(inp.readline())
            nao = [float(x) for x in inp.readline().split()]
            ken = [float(x) for x in inp.readline().split()]
            nao.sort()
            ken.sort()
            dec = deceit(nao, ken)
            nor = war(nao, ken)
            out.write("Case #%d: %d %d\n" % ((case + 1), dec, nor))

def deceit(nao, ken):
    points = 0
    seen = [0] * len(nao)
    for i, m in enumerate(reversed(nao)):
        for j, n in enumerate(reversed(ken)):
            if n < m and seen[j] == 0:
                points += 1
                seen[j] = 1
                break
    return points

def war(nao, ken):
    points = len(nao)
    seen = [0] * len(nao)
    for i, m in enumerate(nao):
        for j, n in enumerate(ken):
            if n > m and seen[j] == 0:
                points -= 1
                seen[j] = 1
                break

    return points
if __name__ == '__main__':
    main(argv)
