t = input()
for i in range(t):
    smax, shyness = raw_input().split()
    smax = int(smax)
    ret = 0
    standing = 0
    for idx, shy in enumerate(shyness):
        if standing < idx and shy != '0':
            ret += (idx-standing)
            standing += idx
        standing += int(shy)
    print "Case #"+str(i+1)+": "+str(ret)
