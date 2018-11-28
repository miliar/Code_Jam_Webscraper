def isTidy(n):
    lastChar = 0
    # print n
    for char in str(n):
        # print char
        if int(char) < lastChar:
            return False
        elif int(char) > lastChar:
            lastChar = int(char)
    return True


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    line = raw_input().split(" ")
    N = int(line[0])
    
    for n in xrange(N, -1, -1):
        # print(n)
        if isTidy(n):
            print "Case #{}: {}".format(i, n)
            break
    
    # if isTidy(N):
    #     print "Tidy!"





    

    
