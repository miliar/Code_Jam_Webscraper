T = input()

for test in xrange(1, T+1):
    smax, s = raw_input().split()
    smax = int(smax)
    stand = 0
    friends = 0
    for shyness in range(smax+1):
        if shyness > stand + friends:
            friends += shyness - (stand + friends)
        stand += int(s[shyness])
    print ('Case #%d: %s' % (test, friends))

        

