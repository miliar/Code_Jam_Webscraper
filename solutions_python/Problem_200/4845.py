tests = int(raw_input())
for test in xrange(tests):
    n = int(raw_input())
    done = False
    z = n
    while not done:
        x = list(str(z))
        if x == sorted(x):
            done = True
            print 'Case #%d: %d' %(test+1, z)
        else:
            z -= 1
