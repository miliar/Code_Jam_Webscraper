import sys

# input
fin = open("C:/Users/Melissa/My Documents/Python/Inputs/C-large.in", 'r')
fout = open("C:/Users/Melissa/My Documents/Python/Outputs/Candy Splitting-large.txt",'w')

T = int(fin.readline().strip())

for i in xrange(1,T+1):

    N = int(fin.readline().strip())
    candy = map(int,fin.readline().strip().split())

    xr = 0
    for nr in candy:
        xr = xr^nr

    if xr <> 0:
        ans = "NO"
    else:
        ans = str(sum(candy) - min(candy))

    print >> fout, "Case #%d: %s" % (i, ans)

fin.close()
fout.flush()
fout.close()     