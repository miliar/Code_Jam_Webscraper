import sys
    
def init():
    print 'begin'
    out = open(sys.argv[2], 'w')
    f = open(sys.argv[1], 'r')
    test_cases = []
    ans = []
    f.readline()
    for line in f:
        tmp = line.split(" ")
	test_cases.append((tmp[0],tmp[1]))


    for t in test_cases:
        hits = 0
        max = int(t[1])
        min = int(t[0])
        n = min
        m = min + 1
        c_max= len(str(n))
        while 1:
            c = c_max
            while 1:
               end = str(n)[c:]
               if str(m) == end + str(n)[:c]:
                   hits +=1
                   break
               c -= 1
               if c == 0:
                   break
            m += 1
            if m > max:
               n +=1  
               m = n +1
            if n > max:
               break
        ans.append(hits)
    ind = 1
    for a in ans:
        out.write("Case #" + str(ind) +": ")
        out.write(str(a))
        out.write("\n")
        ind +=1

init()
