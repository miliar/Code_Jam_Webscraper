import sys
numcases = int(sys.stdin.readline().strip())
#print numcases

for case in range(numcases):
    profit = 0
    (numrides, capacity, numgroups) = [int(i) for i in  sys.stdin.readline().strip().split(' ')]
    groups = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    riders = [] # group to hold riders on board
    #print numrides, capacity, numgroups
    #print groups
    for ride in range(numrides):
        onboard = 0
        while onboard + groups[0] <= capacity:
            onboard += groups[0]
            riders.append(groups.pop(0))
            if len(groups) == 0:
                break
        profit += onboard
        groups += riders # rejoining the queue
        riders = []
    print "Case #" + str(case + 1) + ":", profit
        
