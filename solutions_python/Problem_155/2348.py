from string import maketrans
from sys    import stdin
from re     import findall

test_case = stdin.readline()


def checkIfEnoughAudienceToStandUp(audience, previousStanding = 0,currentStanding = 0):
    finish = 0
    index = 0
    for case in range(1,len(audience)):
        #skipp first audience
        if int(audience[case]) != 0:
            previousStanding += int(audience[case-1])
            if previousStanding == case:
                #previousStanding += int(audience[case])
                #print "Enough audience"
                print previousStanding
            else:
                print "Need add audience"

def checkForOvaltion():
    read_line = lambda: map(str, stdin.readline().split())
    shyness, au = read_line()
    audience = list(au)
    #print audience
    #loop though shyness
    if int(shyness) == 0:
        return 0
    else:
        #checkIfEnoughAudienceToStandUp(audience)
        #return 1
        needAudience = 0
        standingAudience = 0
        finalNeed = 0
        startLooping = 1
        while True:
            standingAudience += int(audience[startLooping-1])
            #print "Standing beginning",standingAudience
            if int(audience[startLooping]) != 0:
                if standingAudience < startLooping:
                    #need add more audience
                    needAudience = startLooping - standingAudience
                    finalNeed += needAudience
                    #print "Need audiend", needAudience
                    standingAudience += needAudience
                    #print "standing audience", standingAudience
            startLooping += 1
            if startLooping == int(shyness) + 1:
                break
        return finalNeed
    

for testCase in xrange(int(test_case)):

    print "Case #%d: %d"%(testCase+1,checkForOvaltion())
