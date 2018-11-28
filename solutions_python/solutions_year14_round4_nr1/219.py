from util import *

def main():
    r = reader("input")
    num = int(r.next())
    ans = []
    for i in xrange(num):
        N,X = map(int, r.next().split(" "))
        files = map(int, r.next().split(" "))
        files.sort(reverse=True)

        disks = []

        for f in files:
            stored = False
            for i in xrange(len(disks)):
                if disks[i] >= f:
                    disks[i] = 0
                    stored = True
                    break
            if not stored:
                disks.append(X - f)

        ans.append(len(disks))
    write("output", ans)

if __name__ == '__main__':
    main()
