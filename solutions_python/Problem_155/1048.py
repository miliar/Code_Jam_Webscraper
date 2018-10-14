import sys
T = int(sys.stdin.readline())
for ttt in range(T):
    caselen, digstr = sys.stdin.readline().split()
    au = 0
    co = 0
    for i in range(len(digstr)):
        if i > au:
            co += 1
            au += int(digstr[i]) + 1
        else:
            au += int(digstr[i])
        print i,' ',co,'dig[i]',int(digstr[i]),' ',au
    print "Case #{}: {}\n".format(ttt+1, co)