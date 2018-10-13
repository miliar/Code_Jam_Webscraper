f = open("C:\Users\Christofer\Documents\GCJ15\A-large.in", "r")
fu = open("C:\Users\Christofer\Documents\GCJ15\out", "w")

t = int(f.readline())

for i in xrange(t):

    line = f.readline().split()
    smax = int(line[0])

    count = 0
    highest = 0

    for x in xrange(len(line[1])):        
        highest = max(highest,max(0,x-count))
        count += int(line[1][x])
    
    fu.write("Case #" + str(i+1) + ": " + str(highest) + "\n")