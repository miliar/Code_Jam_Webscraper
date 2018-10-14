fileName="C:\Users\Paul\A-large.in"
with open(fileName) as f:
    lines = f.read().split("\n")
    T = int(lines[0])
    lines.pop(0)

with open("C:\Users\Paul\output1.txt", "w") as w:
    for x in xrange(T):
        friends=0
        standing=0
        audience = lines[x].split(" ")[1]
        for y in xrange(len(audience)):
            if y==0:
                standing = standing + int(audience[y])
            else:
                diff=0
                if standing<y:
                    diff = (y-standing)
                    # print str(x)+", "+str(diff)
                    friends = friends + diff
                standing = standing + int(audience[y]) + diff
        w.write("Case #"+str(x+1)+": "+str(friends)+"\n")
    print "done"