def getSpeed(D, horses):
    maxTime = 0
    for horse in horses:
        K,S = horse
        time = (D - K)/float(S)
        if(time > maxTime):
            maxTime = time
    return float(D)/maxTime

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    D,N = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    horses = []
    for j in xrange(N):
        K,S = [int(s) for s in raw_input().split(" ")]
        horses.append([K,S])
    constantSpeed = getSpeed(D, horses) # todo
    print "Case #{}: {}".format(i, constantSpeed)