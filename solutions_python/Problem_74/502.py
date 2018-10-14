
f = open('A-large.in')
x = f.readlines()
x.pop(0)


i = 0
for line in x:
    i+=1
    g = line.split()
    g.pop(0)
    steps = [] 
    nextups = {"O":[],"B":[]}
    while len(g):
        steps.append((g[0],int(g[1])))
        nextups[g[0]].append(int(g[1]))
        g.pop(0)
        g.pop(0)
    
#    print nextups
#    print steps

    currentlocs = {"O":0,"B":0}
    time = 0
    while len(steps): 
        actionrobot = steps[0][0]
#        print "ACTIONROBOT %s" % actionrobot
#        print "STEPS: %s" % steps
        target = steps[0][1]
        distance_travelled = abs(target - currentlocs[actionrobot])
        waitingrobot = "O"
        if(actionrobot == "O"):
            waitingrobot = "B"

#        print "NEXTUPS %s" % nextups
#        print "WAITINGROBOT %s" % waitingrobot
        if len(nextups[waitingrobot]):
            waitingtarget = nextups[waitingrobot][0]
            distance_for_waiting = abs(waitingtarget - currentlocs[waitingrobot])
            direc = 1
            if waitingtarget < currentlocs[waitingrobot]:
                direc = -1
            currentlocs[waitingrobot] = currentlocs[waitingrobot] + direc*min(distance_travelled+1,distance_for_waiting)
        

        time += distance_travelled + 1
        currentlocs[actionrobot] = target
        steps.pop(0)
        nextups[actionrobot].pop(0)
#        print 'NEW STEP'
#        print "CURRENT LOCS %s" % currentlocs
       
    print "Case #%d: %d" % (i,time-1)



            
