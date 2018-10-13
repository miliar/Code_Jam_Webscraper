#problem at https://code.google.com/codejam/contest/5304486/dashboard
f = open("A-large.in", "r")
g = open("output.txt","w")
number = int(f.readline())
for i in range(number):
    s = f.readline()
    s = s.split()
    distance = int(s[0])
    horse = int(s[1])
    minihour = 0
    for j in xrange(horse):
        s = f.readline()
        s = s.split()
        d = (distance -int(s[0]))/float(s[1])
        if d>minihour:
            minihour = d
    ans = round(distance/float(minihour),6)
    g.write("Case #" + str(i + 1)+": "+str(ans)+"\n")
