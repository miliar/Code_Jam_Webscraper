f = open("/home/roy/Downloads/A-large.in")

lines = f.readlines()
count = int(lines[0])

#print "There are %s cases" % count

lines = lines[1:]

n = 1
for line in lines:
    if len(line.rstrip()) > 0:
        [N, K] = line.split(" ")
        N = int(N)
        K = int(K)
#        print N
#        print K
        Kp1 = K+1
        Limit = pow(2, N)
#        print Kp1
#        print Limit
        res = Kp1 % Limit
        if res == 0:
            print "Case #%d: ON" % n
        else:
            print "Case #%d: OFF" % n
        n = n+1
        
