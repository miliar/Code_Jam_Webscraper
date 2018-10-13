import sys

def case(c, f, x, t):
    i = c / t
    op1 = (x-c) / t
    op2 = x / (t+f)
    if op1 < op2:
        return i + op1
    else:
        return i + case(c, f, x, t+f)

sys.setrecursionlimit(999999999)
fin = open("B-small.txt")
fout = open("B-small-answer.txt", "w")
t = int(fin.readline())
for i in range(t):
    c, f, x = map(float, fin.readline().split())
    fout.write("Case #%d: %0.7f\n" % (i+1, case(c, f, x, 2)))
fin.close()
fout.close()
