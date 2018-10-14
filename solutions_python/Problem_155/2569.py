
cases = raw_input()
for i in range(int(cases)):
    _, line = raw_input().split() 
    req = 0
    standing = 0
    for shyness, count in enumerate(line):
        extra = 0
        if shyness > standing:
            extra = shyness - standing
            req += extra
        standing += int(count) + extra
    print "Case #%d: %d" %(i+1, req)
