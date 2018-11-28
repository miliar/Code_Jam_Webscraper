import sys

def deceitful_war(naomi, ken):
    naomi = naomi[:]
    ken = ken[:]
    n = 0

    for nblock in naomi:
        if ken[0] > nblock:
            ken.pop()
        else:
            n += 1
            ken.pop(0)

    return n

def war(naomi, ken):
    naomi = naomi[:]
    ken = ken[:]
    n = 0

    for nblock in naomi:
        try:
            kblock = min(block for block in ken if block > nblock)
        except ValueError:
            kblock = ken[0]

        ken.remove(kblock)
        if kblock < nblock:
            n += 1

    return n

def main():
    with open(sys.argv[1]) as f:
        lines = [l.rstrip() for l in f.readlines()[1:]]

    data = zip(lines[1::3], lines[2::3])

    for i, (naomi, ken) in enumerate(data, 1):
        naomi = sorted(map(float, naomi.split()))
        ken = sorted(map(float, ken.split()))

        y = deceitful_war(naomi, ken)
        z = war(naomi, ken)
        print 'Case #{0}: {1} {2}'.format(i, y, z)

if __name__ == '__main__':
    main()
