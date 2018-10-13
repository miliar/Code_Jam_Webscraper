def solve(low, high, others):
    for note in range(low, high + 1):
        okay = True
        for other in others:
            if note % other != 0 and other % note != 0:
                okay = False
        if okay:
            return str(note)
    return "NO"

f = file("input.txt")
lines = f.readlines()
line = 0
for t in range(1, int(lines[line]) + 1):
    line += 1
    tcdat = [int(dat) for dat in lines[line].split(" ")]
    l = tcdat[1]
    h = tcdat[2]
    line += 1
    o = [int(dat) for dat in lines[line].split(" ")]
    print "Case #" + str(t) + ": " + solve(l, h, o)
