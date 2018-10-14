import math, collections
f = open('input.in','r')
g = open('output.txt','w')
"""
just a basic string problem
"""
for index in xrange(1, int(f.readline()[:-1]) + 1):
    N = f.readline()[:-1]
    length = len(N)
    if length == 1:
        result = N
    else:
        flag = -1
        for i in xrange(length-1):
            if N[i] > N[i+1]:
                flag = i
                break
        if flag == -1:
            result = N
        elif flag == 0:
            result = str(int(N[0])-1) + '9'*(length-1) if N[0] > '1' else '9'*(length-1)
        else:
            flag2 = -1
            for i in xrange(flag-1, -1, -1):
                if N[i] < N[i+1]:
                    flag2 = i + 1
                    break
            if flag2 == -1:
                result = str(int(N[0])-1) + '9'*(length-1) if N[0] > '1' else '9'*(length-1)
            else:
                result = N[:flag2] + str(int(N[flag2])-1) + '9'*(length-flag2-1)
    g.write("Case #{}: {}\n".format(index, result))
    print "Case #{}: {}\n".format(index, result)
f.close()
g.close()