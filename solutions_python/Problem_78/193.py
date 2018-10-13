#!/home/chenfzh/bin/python


def gnd(x,y):
    l = min(x,y)
    u = max(x,y)
    while l != 0:
        t = l
        l = u % l
        u = t
    return u

def calc(ndg):
    df = ndg[2] - ndg[1]
    if (ndg[2] == 0 and ndg[1] != 0) or (ndg[2] == 100 and ndg[1] != 100):
        return 'Broken'
    if (ndg[2] == 0 and ndg[1] == 0) or (ndg[2] == 100 and ndg[1] == 100):
        return 'Possible'
    if ndg[1] == 0 or ndg[0] >= 100 / gnd(100, ndg[1]): 
        return 'Possible'
    return 'Broken'

def readfile(filename):
    f = open(filename)
    c = f.readlines()
    f.close();
    res = []
    for i in c[1:]:
        res.append([int(x) for x in i.split()])
    return res

if __name__ == '__main__':
    import sys
    lines = readfile(sys.argv[1])
    for i in range(len(lines)):
        print('Case #%d: %s' % (i + 1, calc(lines[i])))
