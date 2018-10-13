import string, sys


f = open("output.txt", "w+")
count = 0
N = 0
for line in sys.stdin:
    if count > 0:
        if (count > N + 1):
            break
        m, l = [item for item in line.split()]
        res = 0
        i = 0
        total = 0
        for c in l:
            n = int (c)
            if ( (i > total) & (n != 0) ):
                res += i - total
                total += i - total
            total += n
            i = i + 1
        f.write('Case #%s: %s\n' % (count,res))
    else:
        N = int(line)
    count = count + 1

