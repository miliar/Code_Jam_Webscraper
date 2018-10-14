t = int(raw_input())
for i in xrange(1, t+1):
    n = int(raw_input())
    x = n
    while True:
        flag = False
        x = str(x)
        for j in xrange(1, len(x)):
            if x[j-1] > x[j]:
                flag = True
                break
        if flag: #not found
            x = int(x) - 1
        else:
            print "Case #"+str(i)+": "+str(x)
            break



