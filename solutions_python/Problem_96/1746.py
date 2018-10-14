import sys

def nominus(i):
    if i < 0:
        i = 0
    return i

def get_the_number_of_googler(l):
    N = l[0]
    S = l[1]
    p = l[2]
    t = list()
    r = 0
    for i in range(3, 3+N):
        t.append(l[i])
    for x in t:
        if x >= nominus(p-1)*2+p:
            r = r + 1
        elif S > 0 and x >= nominus(p-2)*2+p:
            r = r + 1
            S = S - 1
    return r

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        f = open(filename)

    lines = f.read().splitlines()
    cases = int(lines[0])
    for i in range(1, cases + 1):
        splitted = lines[i].split(' ')
        for e, x in enumerate(splitted):
            splitted[e] = int(x)
        print "Case #%i: %i" % (i, get_the_number_of_googler(splitted))
