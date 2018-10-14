f = open('D-large.in', 'r')
cases = int(f.readline())
for case in range(cases):
    nNum = f.readline()
    line = f.readline()
    l = [int(s) for s in line.split()]

    num = 0.0
    for i,el in enumerate(l):
        ind = i+1
        if el != ind:
            num+=1

    print "Case #%s: %s" % (case+1, num)


