import sys

# input
fin = open("C:/Users/Melissa/My Documents/Python/Inputs/D-large.in", 'r')
fout = open("C:/Users/Melissa/My Documents/Python/Outputs/GoroSort-large.txt",'w')

T = int(fin.readline().strip())

for i in xrange(1,T+1):

    N = int(fin.readline().strip())
    inline = map(int, fin.readline().strip().split())

    count = 0
    for nr in inline:
        if nr <> (inline.index(nr) + 1):
            count += 1
    
    print >> fout, "Case #%d: %.6f" % (i, count)

fin.close()
fout.flush()
fout.close()     