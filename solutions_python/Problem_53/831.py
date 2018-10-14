with open("C:\\A-large.out", 'w') as w:
    with open("C:\\A-large.in") as f:
        cases = int(f.readline().rstrip('\n'))
        for i in xrange(cases):
            s = f.readline().rstrip('\n').split()
            snappers = int(s[0])
            snaps = int(s[1])
            res = bin(snaps)
            if res[len(res)-snappers:] == "1"*snappers:
                w.write("Case #%d: ON\n" % (i+1))
            else:
                w.write("Case #%d: OFF\n" % (i+1))
    
        
