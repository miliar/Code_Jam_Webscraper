import sys
for case,line in enumerate(open(sys.argv[1]).readlines()[1:]):
    print 'Case #%d: %s' % (case+1, "ON" if (((int(line.strip().split(' ')[1])+1) % 2**int(line.strip().split(' ')[0])) == 0) else "OFF")
