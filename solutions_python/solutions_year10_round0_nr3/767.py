# May, 8, 2010
# Qualification Round
# "Theme Park"

from time import time

#inpath = "C-sample.in"
#inpath = "C-large.in"
inpath = 'C-small-attempt0.in'
outpath = "C.out"

timestart = time()

fin = open(inpath)
fout = open(outpath, 'w')

def Gain (R, k, N, groups):
    money = 0
    current = 0
    end = 0
    for i in range(R):
        if groups[current] > k:
            return money
        seats = k
        while groups[current] <= seats:
            seats -= groups[current]
            money += groups[current]
            current = (current+1)%N
            if current == end:
                break
        end = current
    return money

T = int(fin.readline())
for case in range(1, T+1):
    R, k, N = map(int, fin.readline().split())
    groups = map(int, fin.readline().split())
    fout.write("Case #%d: %d\n" % (case, Gain(R, k, N, groups)))
    #print case

fin.close()
fout.close()
print "%.4f" % (time() - timestart)
