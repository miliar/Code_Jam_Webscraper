import math

def run(d, k, s):
    n = len(k)
    maxt = 0
    for i in xrange(n):
        maxt = max(maxt, (d - k[i]) * 1.0 / s[i])
    speed = d / maxt
    return str(speed)

inputfilename = "A-large.in"
fin = open(inputfilename, "r")
outputfilename = "cruise_control_output.txt"
fout = open(outputfilename, "w")
t = fin.readline()
t = int(t)
for i in xrange(1, t+1):
    line = fin.readline().split(" ")
    d = int(line[0])
    n = int(line[1])
    k = []
    s = []
    for j in xrange(n):
        line = fin.readline().split(" ")
        k.append(int(line[0]))
        s.append(int(line[1]))
    result = "Case #" + str(i) + ": " + run(d, k, s) + '\n'
    fout.write(result)

fin.close()
fout.close()
