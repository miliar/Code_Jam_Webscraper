
class Robot():
    pos=1 #position
    walkTime=0 #time to walk to next button

    def press(self, k):
        dist = abs(k - self.pos) #distance to walk
        dist = dist - self.walkTime #assume walked towards button
        dist = max(0, dist) #don't walk too far
        time = dist + 1 #takes a second to push button
        self.pos = k
        self.walkTime = 0
        return time

def pressesToTime(presses):
    o = Robot()
    b = Robot()
    totalTime = 0
    
    for press in presses:
        robot, button = press
        if (robot == 'O'):
            time = o.press(button)
            b.walkTime += time
            totalTime += time
            #print("Time:", totalTime, " O:", o.pos)
        elif (robot == 'B'):
            time = b.press(button)
            o.walkTime += time
            totalTime += time
            #print("Time:", totalTime, " B:", b.pos)
        
    return totalTime

def strToPresses(strIn):
    vals = strIn.split()[1:] #remove the number of test cases
    presses = [[vals[i], int(vals[i+1])] for i in range(0,len(vals),2)]
    return presses

def solve(inF, outF):
    """usage: solve('in.txt', 'out.txt')"""
    fIn = open(inF, 'r')
    fOut = open(outF, 'w')
    
    cases = int(fIn.readline())
    for case in range (1, cases+1):
        presses = strToPresses(fIn.readline())
        TotalTime = pressesToTime(presses)
        soln = "Case #" + str(case) + ": " + str(TotalTime)
        print (soln)
        fOut.write(soln + '\n')

    fIn.close()
    fOut.close()

        
  
    
