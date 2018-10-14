numcases = int(input())
for numcase in range(numcases):
    inputs = list(map(float, input().split(' ')))
    farmcost, farmcookierate, goal = inputs[0], inputs[1], inputs[2]

    cookierate = 2
    cookies = 0
    seconds = 0

    while cookies < goal:
        #print(seconds, cookies, cookierate)
        timetofinish = (goal - cookies) / cookierate
        timetonextfarm = (farmcost - cookies) / cookierate
        timetofinishwithnextfarm = timetonextfarm + goal / (cookierate + farmcookierate)
        #print(timetofinish, timetonextfarm, timetofinishwithnextfarm)
        if timetofinish <= timetonextfarm or timetofinish <= timetofinishwithnextfarm:
            cookies = goal
            seconds += timetofinish
            #print('finishing!')
        elif cookies >= farmcost:
            cookies -= farmcost
            cookierate += farmcookierate
            #print('buying farm')
        else:
            cookies = farmcost
            seconds += timetonextfarm
            #print('going to next decision point!')

    print('Case #%s: %s ' % (numcase + 1, seconds))
        
    
