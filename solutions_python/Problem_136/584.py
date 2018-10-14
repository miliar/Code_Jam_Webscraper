from string import *

def read_words(filename):
    '''
    converts a file to a list
    '''
    
    words = []
    for line in filename:
            words.append(line.strip())
    return words

filename = open("coddy.txt", 'r')
numcases = int(filename.readline())

def take_next_farm(cost, bonus, goal, cookies, rate):
    nofarm = (goal - cookies)/rate
    withfarm = (cost/rate) + (goal)/(rate + bonus)
    #print
    #print "nofarm: "
    #print nofarm
    #print "withfarm: "
    #print withfarm
    #print
    return (withfarm < nofarm)

for casenum in range (numcases):
    info = filename.readline()
    info = split(info)
    
    farmcost = float(info[0])
    farmbonus = float(info[1])
    goal = float(info[2])
    
    cookies = 0.0
    currentrate = 2.0
    elapsed = 0.0
    #print cookies
    
    while (cookies < goal):
        if (take_next_farm(farmcost, farmbonus, goal, cookies, currentrate)):
            #print "taking the farm. Adding: " + str((farmcost/currentrate))
            elapsed+=(farmcost/currentrate)
            currentrate += farmbonus

        else:
            #print "adding: " + str(((goal-cookies)/currentrate))
            elapsed +=((goal-cookies)/currentrate)
            cookies+=(goal)
    result = ''
    result+= "Case #" + str(casenum + 1) + ": "   
    result+= str(elapsed)
    print result
            
    