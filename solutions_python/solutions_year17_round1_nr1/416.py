t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}:".format(i)
    success = False
    num = 0
    lastoutstr = ''
    for i in range(0, n):
        line = str(raw_input())
        outstr = ''
        lastind = -1
        last = '?'
        for z in range(0, m):
            #print success
            #print str(z) + str(line[z]) + last + str(success)
            if (line[z] != '?'):
                last = line[z]
                outstr = outstr + last * (z - lastind)
                lastind = z
                if (z == m-1):
                    if not success:    
                        success = True
                        for i in range(0, num):
                            print outstr
                    lastoutstr = outstr
            if (z == (m-1) and line[z] == '?' and last != '?' and success):
                outstr = outstr + last * (z - lastind)
                lastoutstr = outstr
            if (z == (m-1) and line[z] == '?' and last != '?' and (not success)):
                success = True
                outstr = outstr + last * (z - lastind)
                lastoutstr = outstr
                for i in range(0, num):
                    print outstr
            if (z == (m-1) and line[z] == '?' and last == '?' and success):
                outstr = lastoutstr
            if (z == (m-1) and line[z] == '?' and last == '?' and not success):
                num = num + 1
        if success:
            print outstr
