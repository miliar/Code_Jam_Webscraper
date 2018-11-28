infile = open('in')
outfile = open('out','w')

n = int(infile.readline())
for i in range(n):
    #print()
    cost,farm,target = [float(i) for i in infile.readline().split()]
    rate = 2
    totaltime = 0
    time = target/rate
    newtime = cost/rate + target/(rate+farm)
    #print(cost/rate , target/(rate+farm), newtime)
    while newtime < time:
        totaltime += cost/rate
        rate += farm
        time = target/rate
        newtime = cost/rate + target/(rate+farm)
        #print(cost/rate , target/(rate+farm), newtime)
    totaltime += time
    outfile.write('Case #' + str(i+1) + ": " + str(totaltime) + '\n')
