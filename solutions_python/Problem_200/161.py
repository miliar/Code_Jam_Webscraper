def f(line):
    line = list(line)
    tidy = False
    while not tidy:
        for i in xrange(len(line)-1):
            if line[i] > line[i+1]:
                break
        else:
            tidy = True
        
        if not tidy:
            line[i] = str(int(line[i])-1)
            for j in xrange(i+1,len(line)):
                line[j] = '9'
            # print line
    return int(''.join(line))
        
T = int(raw_input())
for i in xrange(1,T+1):
    print "Case #%d: %s" % (i, f((raw_input())))
    
    # 5
    # 0
    # 1
    # 2
    # 11
    # 1692Square Brackets [ ] | English Club