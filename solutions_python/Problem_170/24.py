#filePath = 'data.in'
filePath = 'C-small-attempt0.in'

m = n = 0
string = []

def check(fr, to):
    record = set([])
    for x in fr:
        if x in to:
            record.add(x)
    return len(record)

def read(f):
    global n, string
    n = int(f.readline().strip())
    string = []
    for _ in xrange(n):
        string.append(f.readline().strip().split())


def solve():
    ans = -1
    for i in xrange(2 ** (n-2)):
        e = [x for x in string[0]]
        f = [x for x in string[1]]
        for j in xrange(n-2):
            st = (i >> j) & 1
            if st == 0: e.extend(string[j+2])
            else: f.extend(string[j+2])
        e = set(e)
        f = set(f)
        #tmp = check(e, f)
        tmp = len(e.intersection(f))

        if ans == -1 or tmp < ans:
            ans = tmp

    print ans

    return

def main():
    with open(filePath, 'r') as f:
        cas = int(f.readline())
        for _ in xrange(1,cas+1):
            print "Case #%d:" % _,
            read(f)
            solve()
    f.close()

    return

if __name__ == '__main__':
    main()
