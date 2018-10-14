import sys

global mapping


def decode():
    base = {
        'a zoo':
            'y qee',
        'ejp mysljylc kd kxveddknmc re jsicpdrysi':
            'our language is impossible to understand',
        'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd':
            'there are twenty six factorial possibilities',
        'de kr kd eoya kw aej tysr re ujdr lkgc jv':
            'so it is okay if you want to just give up'
    }

    global mapping
    mapping = {}

    for o, t in base.items():
        o_s = [l for l in o]
        t_s = [l for l in t]
        z_l = zip(o_s, t_s)
        for z in z_l:
            mapping[z[0]] = z[1]

    k = mapping.keys()
    v = mapping.values()
    mapping[list(set(v) - set(k))[0]] = list(set(k) - set(v))[0]


def solve(txt):
    global mapping
    out = ''
    for l in txt:
        out += mapping[l]
    return out


def main(filename):
    with open(filename, "r") as f:
        T = int(f.readline().strip())
        for t in xrange(1, T + 1):
            txt = f.readline().strip()
            print "Case #%d: %s" % (t, solve(txt))


if __name__ == "__main__":
    decode()
    main(sys.argv[1])
