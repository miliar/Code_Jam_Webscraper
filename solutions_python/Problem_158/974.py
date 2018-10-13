inf = open('i4.txt', 'r')
outf = open('o4.txt', 'w')
lines = list(inf)
inf.close()

cnt = int(lines[0])
for i in range(1, cnt+1):
    splitline = lines[i].split(' ')
    x = int(splitline[0])
    r = int(splitline[1])
    c = int(splitline[2])
    ans = 'GABRIEL'
    if (r * c) % x != 0:
        ans = 'RICHARD'
    if x > 2 and x / 2 >= min(c, r):
        ans = 'RICHARD'
    if x >= 7:
        ans = 'RICHARD'
    outf.write("Case #" + str(i) + ": " + str(ans) + "\n")

outf.close()

 #
##
#
