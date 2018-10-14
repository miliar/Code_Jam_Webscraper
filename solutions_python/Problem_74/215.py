#!/home/chenfzh/bin/python

def readfile(filename, srb):
    f = open(filename)
    c = f.readlines()[1:]
    f.close()
    for i in c:
        t = i.split()[1:]
        s = []
        r = []
        b = []
        for j in range(0, len(t)):
            if j % 2 == 0:
                s.append((t[j], int(t[j + 1])))
                if t[j] == 'O':
                    r.append(int(t[j + 1]))
                else:
                    b.append(int(t[j + 1]))
        srb.append((s,r,b))


def calc(s, r, b):
    i = 0
    rl = 1
    bl = 1
    while (len(s) > 0):
        i += 1
        if s[0][0] == 'O':
            if rl == s[0][1]:
                s = s[1:]
                r = r[1:]
            elif rl < s[0][1]:
                rl += 1
            else:
                rl -= 1
            if len(b) > 0:
                if bl > b[0]:
                    bl -= 1
                elif bl < b[0]:
                    bl += 1
        else:
            if bl == s[0][1]:
                s = s[1:]
                b = b[1:]
            elif bl < s[0][1]:
                bl += 1
            else:
                bl -= 1
            if len(r) > 0:
                if rl > r[0]:
                    rl -= 1
                elif rl < r[0]:
                    rl += 1
    return i

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print("usage: %s <filename>" % sys.argv[0])
        exit(0)
    srb = []
    readfile(sys.argv[1], srb)
    for i in range(0, len(srb)):
        print("Case #%d: %d" % (i + 1, calc(srb[i][0], srb[i][1], srb[i][2])))
