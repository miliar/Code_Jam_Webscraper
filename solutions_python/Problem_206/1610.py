inf = open('input.txt', 'r')
outf = open('output.txt', 'w+')
t = int(inf.readline())
for ct in range(t):
    k, d = map(int, inf.readline().split())
    time = -1.0;
    for i in range(d):
        m, s = map(int, inf.readline().split())
        distance = k - m
        hour = float(distance) / s
        if hour > time:
            time = hour
    outstring = "Case #%d: %.6f\n" %(ct+1, k / time)
    outf.write(outstring)
