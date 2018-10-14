T = int(raw_input())

for t in range(T):
    line = raw_input().split()
    sMax = int(line[0])
    s  = line[1]

    extra = 0
    total = 0
    
    for c in range(sMax+1):
        if c > total + extra:
            extra = c - total

        total += int(s[c])

    print "Case #" + str(t+1) + ": " + str(extra)
