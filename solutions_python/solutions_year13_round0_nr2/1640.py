import sys, string

def mow(n, m, lawn):
    hormin = []
    vermin = []
    tr = zip(*lawn)
    for ni in range(n):
        row = lawn[ni]
        allsame = reduce(lambda a, b: a if a == b else 1000, row) != 1000
#        print row, allsame
        hormin.append(1000 if allsame else min(row))
    for mi in range(m):
        col = tr[mi]
        allsame = reduce(lambda a, b: a if a == b else 1000, col) != 1000
        vermin.append(1000 if allsame else min(col))
#    print hormin, "\n", vermin
            
    for ni in range(n):
        row = lawn[ni]
        for mi in range(m):
	    el = row[mi]
            if hormin[ni] == el and vermin[mi] == el: return 'NO'
    return 'YES'

def main(args):
    f = file(args[1])
    ncases = int(f.readline())
    for i in range(ncases):
        line = f.readline().rstrip()
        parts = line.split()
        nums = map(int, parts)
        n, m = nums
        lawn = []
        for ni in range(n):
            line = f.readline().rstrip()
            lawn.append(map(int, line.split()))
        ans = mow(n, m, lawn)
        sys.stdout.write("Case #%d: %s\n" % (i+1, ans))

if __name__ == "__main__":
    main(sys.argv)