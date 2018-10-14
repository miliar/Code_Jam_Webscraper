#!/home/chenfzh/bin/python



def calc(line):
    l = line[0]
    t = line[1]
    n = line[2]
    c = line[3]
    dist = (line[4:] * (n / c + 1))[0 : n]
    total = sum(dist) * 2
    r = t / 2
    for i in range(0, len(dist)):
        if r > dist[i]:
            r -= dist[i]
            dist[i] = 0
        else:
            dist[i] -= r
            break
    s = 0
    for i in range(0, l):
        m = max(dist)
        s += m
        dist.remove(m)
    return total - s

def readfile(filename):
    f = open(filename)
    c = f.readlines()[1:]
    f.close()
    res = []
    for i in c:
        res.append([int(x) for x in i.split()])
    return res

if __name__ == '__main__':
    import sys
    lines = readfile(sys.argv[1])
    for i in range(0, len(lines)):
        print('Case #%d: %d' % (i+1, calc(lines[i])))
