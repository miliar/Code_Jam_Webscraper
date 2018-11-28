__author__ = 'Mert'

inp = open("inp.txt")
o = open("o.txt",'w')
t = int(inp.readline())
for i in xrange(t):
    s = inp.readline()
    l = s.split(' ')
    maxT = int(l[0])
    s = l[1]
    count = 0
    peopleNeeded = 0
    for j in xrange(maxT+1):
        a = int(s[j])
        b = 0
        if a > 0 and count < j:
            b = j - count
        peopleNeeded = peopleNeeded + b
        count = count + b + a
    o.write("Case #" + str(i+1) + ": " + str(peopleNeeded) + "\n")