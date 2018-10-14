T = int(raw_input())

for x in xrange(1,T+1):

    line = raw_input().split()
    N = int(line[0])
    Pd = int(line[1])
    Pg = int(line[2])
    flag = 0

    if Pd == 0 and Pg == 0:
        flag = 1
    elif Pd == 100 and Pg == 100:
        flag = 1
    elif Pg == 0 or Pg == 100:
        flag = 0
    else:
        for i in xrange(1,N+1):
            if i*Pd/100.0%1 == 0:
                flag = 1
                break

    if flag == 1:
        print "Case #%d: Possible" %x
    else:
        print "Case #%d: Broken" %x
