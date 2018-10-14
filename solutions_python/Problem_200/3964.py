##    line = f.readline().rstrip().split(' ')
##    pancakes = line[0]
##    spatula = line[1]
##
##    flips = pancakes.count('-+') + pancakes.count('+-')
##
##    if flips < spatula
##                
def isAsc(N_str):
    for i in range(len(N_str)):
        if i+1 != len(N_str):
            diff = int(N_str[i]) - int(N_str[i+1])
            if diff > 0:
                return False
    return True


t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    N_str = str(raw_input())
    
    for j in xrange(int(N_str), -1, -1):
        N_str = str(j)
        if j < 10:
            print "Case #{}: {}".format(i, j)
            break
        elif isAsc(N_str):
            print "Case #{}: {}".format(i, j)
            break

