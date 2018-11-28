def workcost(a, m):
    x = a
    cost = []
    for i in range(len(m)):
        inc = x - 1
        c = 0
        if inc == 0:
            c = len(m) + 1 #can't grow
        else:
            while x <= m[i]:
                x += inc
                inc *= 2
                c += 1
            x += m[i]
        cost.append(c)
    return cost

# starts here
import sys
l = sys.stdin.readline()
count = int(l)

for i in range(count):
    a, n = sys.stdin.readline().split()
    a = int(a)
    motesStr = sys.stdin.readline().split()
    motes = [int(s) for s in motesStr]
    motes.sort()
    cost = workcost(a, motes)
    #now we have a cost list
    #scan backwards to find out whether it should be kept or forget

    l = len(cost)
    throw = l
    for j in range(l - 1, -1, -1):
        #print 'cost', cost[j], j, l - j
        if cost[j] >= throw - j:
            throw = j

    step = l - throw
    #print step, throw
    for j in range(throw):
        step += cost[j]
        #print j, step

    print "Case #" + str(i+1) + ": " + str(step)
    
