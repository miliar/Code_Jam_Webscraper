infile = open('B-small-attempt0.in','r')
outfile = open('cookie.out.txt','w')

cases = int(infile.readline().strip())
for case in range(1,cases+1):
    inps = infile.readline().strip().split()
    [C,F,X] = [float(inps[0]),float(inps[1]),float(inps[2])]

    besttime = float("inf")
    numcookiefarms = 0
    
    while True:
        rate = 2.0
        time = 0.0
        for i in range(numcookiefarms):
            timetillnextcookiefarm = C/rate
            time += timetillnextcookiefarm
            rate += F
        time += X/rate
        if time >= besttime:
            break
        else:
            besttime = time
            numcookiefarms += 1
    outfile.write('Case #'+str(case)+': '+str(besttime)+'\n')

outfile.close()
