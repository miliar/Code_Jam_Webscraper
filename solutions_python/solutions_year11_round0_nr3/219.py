#!/home/chenfzh/bin/python


def calc(s):
    r = 0
    for i in s:
        r ^= i
    if r != 0:
        return "NO"
    return "%s" % (sum(s) - min(s))
    

def readfile(filename):
    lines = []
    f = open(filename)
    c = f.readlines()[1:]
    f.close()
    for i in range(0, len(c)):
        if i % 2 != 0:
            lines.append([int(x) for x in c[i].split()])
    return lines

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        exit(0)
    cnt = 1
    for i in readfile(sys.argv[1]):
        print("Case #%d: %s" % (cnt, calc(i)))
        cnt += 1
