import sys

def solve(l):
    (N, R, O, Y, G, B, V) = l
    N = int(N)
    names = ["N", "R", "O", "Y", "G", "B", "V"]
    priority = []

    for i in range(1, len(l)):
        prioriVal = 0
        priority.append((int(l[i]), prioriVal, names[i]))

    res = ""
    last = "-"
    priority.sort(reverse=True)
    priority[0] = (priority[0][0], 1, priority[0][2])

    while N > 0:
        N -= 1
        priority.sort(reverse=True)

        i = 0
        while priority[i][2] == last: # TODO update incomaptibility rule
            if priority[i][0] == 0:
                return "IMPOSSIBLE"
            i+=1
        if priority[i][0] == 0:
            return "IMPOSSIBLE"
        last = priority[i][2]
        res += last
        priority[i] = (priority[i][0]-1, priority[i][1], priority[i][2])
    if res[0] == res[-1]:
        return "IMPOSSIBLE"
    priority.sort(reverse=True)
    if priority[0][0] != 0:
        print ""
        print ""
        print "=================================================== BUG ==================================================="
        print ""
        print ""

    return res

def parse(s):
    l = s.split(" ")
    
    return solve(l)

def process(filenamein):
    f = open(filenamein, "r")
    size = int(f.readline())
    for line in xrange(size):
        s = f.readline()
        res = parse(s)
        out = "Case #" + str(line+1) + ": " + res
        print out
    f.close()

if len(sys.argv) == 2:
    process(sys.argv[1])