import sys

def main(args):
    input = open(args[0])
    cases = int(input.readline())
    for i in range(cases):
        casenum = i + 1
        casein = input.readline().split(" ")
        numbooster = int(casein[0])
        boostertime = int(casein[1])
        numstars = int(casein[2])
        c = int(casein[3])
        dists = []
        for dist in range(c):
            dists.append(int(casein[4 + dist]))
        
        stars = []
        for star in range(numstars):
            #how long will it take me to get here?
            timetohere = 0
            #what's the value of putting a booster on this star?
            if(len(stars) > 0):
                #this is not the first star
                timetohere = stars[-1][0] + stars[-1][1]
            
            disttonext = dists[star % c]
            
            timetonext = disttonext * 2
            if((timetohere + timetonext) < boostertime):
                value = 0
            elif(timetohere < boostertime):
                slowhours = boostertime - timetohere
                slowdist = slowhours / 2
                fastdist = disttonext - slowdist
                newtime = (slowdist * 2) + fastdist
                value = timetonext - newtime
            else:
                value = disttonext
            #print "Star {0}: {1} ({2})".format(star, disttonext, value)
            stars.append((timetohere, timetonext, value))
        
        stars.sort(key=lambda star: star[2], reverse=True)
        result = 0
        for star in stars:
            result = result + star[1]
            if(numbooster > 0):
                numbooster = numbooster - 1
                result = result - star[2]
        
        print "Case #{0}: {1}".format(casenum, result)
        #print combinations
        #print oppositions
        

if __name__ == '__main__':
    main(sys.argv[1:])