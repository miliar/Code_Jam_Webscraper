fin = open('B-large.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())

for i in xrange(t):
    c, f, x = fin.readline().split()
    c = float(c)
    f = float(f)
    x = float(x)
    result = 0.0
    cps = 2.0
    while(c/cps + x/(cps + f) < x/cps):
        result += c/cps
        cps += f
    result += x/cps

    fout.write('Case #' + str(i + 1) + ': ' + str(result) + '\n')

fout.close()

