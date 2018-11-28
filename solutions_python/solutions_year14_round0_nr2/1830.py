infile = r'C:\Users\PK GUPTA\Downloads\B-large.in'
outfile = r'C:\Users\PK GUPTA\Downloads\B-large-attempt0-output.txt'

ifp = open(infile, 'r')
t=int(ifp.readline().strip())
answer=''
for i in range(t):
    rate=2.0
    c,f,x=map(float, ifp.readline().strip().split(' '))
    maxtime = x/rate
##    print c,f,x

    timestep = 0.0
    rate = 2.0
    totaltime = 0.0
    cookietime = x/rate
    farmtime = 0.0
    totaltime = cookietime + farmtime
##    print timestep, rate, farmtime, cookietime, totaltime

    while True:
        #next time step
        timestep += 1
        farmtime += c/rate
        rate += f
        cookietime = x / rate
        newtotaltime = cookietime + farmtime
##        print timestep, rate, farmtime, cookietime, newtotaltime

        if newtotaltime > totaltime:
            break
        totaltime = newtotaltime
        
    finaltime = totaltime
    
    if finaltime>maxtime:
        finaltime = maxtime
        print 'Fail'
        
    print 'Case #%d: %1.7f\n' %(i+1, finaltime)
    answer += 'Case #%d: %1.7f\n' %(i+1, finaltime)


ifp.close()
##print answer
ofp = open(outfile, 'w')
ofp.write(answer)
ofp.close()

