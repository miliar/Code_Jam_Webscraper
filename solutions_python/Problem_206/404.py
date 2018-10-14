fin = open('A-large.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())

for i in xrange(t):
    d, n = map(int, fin.readline().split())
    time = 0
    for j in xrange(n):
        k, s = map(int, fin.readline().split())
        tim = float(d - k)/float(s)
        if tim > time:
            time = tim
    answer = d/time
    
    fout.write("Case #" + str(i + 1) + ": " + str(answer) + "\n")
fout.close()
