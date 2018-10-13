class TestCase():
    def __init__(self, CAct, JAct):
        self.CAct = CAct
        self.JAct = JAct


    def countExchange(self, schedule):
        count = 0
        lastChar = schedule[-1][2]
        for k in range(len(schedule)):
            if not schedule[k][2] == lastChar:
                lastChar = schedule[k][2]
                count+=1
        return count 
    def getTimeDiff(self, scheduleEntry):
        tmp = scheduleEntry[1] - scheduleEntry[0]
        if tmp <= 0:
            tmp += 1440
        return tmp
    
    def getTimes(self, schedule):
        cTime = 0
        jTime = 0

        for t in schedule:

            if t[2] == "C":
                cTime += self.getTimeDiff(t)
            elif t[2] == "J":
                jTime += self.getTimeDiff(t)
        return (cTime, jTime)

    def splitEntry(self, scheduleEntry, time, leftchar, rightchar):
        out = [list(scheduleEntry[:]), list(scheduleEntry[:])]
        out[0][1] = (time + scheduleEntry[0])%1440
        if leftchar:
            out[0][2] = leftchar
        out[1][0] = (time + scheduleEntry[0])%1440
        if rightchar:
            out[1][2] = rightchar
        return out
        

    def addTime(self, schedule, char, maxtime):
        bestNeighbor = (0, 0)
        best = (0,0)
        dyn_indices = []
        for i in range(len(schedule)):
            if schedule[i][3] == "DYN" and not schedule[i][2] == char:
                dyn_indices.append(i)
        for i in dyn_indices:
            val = self.getTimeDiff(schedule[i])
            if val > best[1]:
                best = (i, val)
            if(schedule[i-1][2] == char):
                if val > bestNeighbor[1]:
                    bestNeighbor = (i, val)
            if i+1 == len(schedule):
                if schedule[0][2] == char:
                    if val > bestNeighbor[1]:
                        bestNeighbor = (i, val)
            else:
                if schedule[i+1][2] == char:
                    if val > bestNeighbor[1]:
                        bestNeighbor = (i, val)
        if not bestNeighbor == (0, 0):
            if bestNeighbor[1] < maxtime:
                schedule[bestNeighbor[0]][2] = char
                return schedule
            else:
                #find left or right
                
                if schedule[bestNeighbor[0]-1][2] == char:
                    return schedule[:bestNeighbor[0]] + self.splitEntry(schedule[bestNeighbor[0]], maxtime, char, "") + schedule[bestNeighbor[0]+1:]
                else:
                    return schedule[:bestNeighbor[0]] + self.splitEntry(schedule[bestNeighbor[0]], getTimeDiff(schedule[bestNeighbor[0]])-maxtime, "", char) + schedule[bestNeighbor[0]+1:]
        else:
            
            if best[1] < maxtime:
                schedule[best[0]][2] = char
                return schedule
            else:
                return schedule[:best[0]] + self.splitEntry(schedule[best[0]], maxtime, char, "") + schedule[best[0]+1:]
                
    def solve(self):
        scheduledict = {}
        for t in self.CAct:
            scheduledict[t[0]] = (t[0], t[1], "C", "STA")
        for t in self.JAct:
            scheduledict[t[0]] = (t[0], t[1], "J", "STA")

        s = sorted(scheduledict)

        schedule = []
        for i in range(len(s)):
            if not (scheduledict[s[i-1]][1] ==  scheduledict[s[i]][0]):
                schedule.append(list((scheduledict[s[i-1]][1], scheduledict[s[i]][0], scheduledict[s[i]][2], "DYN")))
            schedule.append(list(scheduledict[s[i]]))

        (cTime, jTime) = self.getTimes(schedule)
        while not cTime == jTime:

            if cTime < jTime:
                schedule = self.addTime(schedule, "C", int((jTime - cTime)/2))
            elif jTime < cTime:
                schedule = self.addTime(schedule, "J", int((cTime - jTime)/2))
            (cTime, jTime) = self.getTimes(schedule)


        
        
        

                

        return self.countExchange(schedule)
            

                

            

            


def loadTestCases(taskChar, path):
    out = []
    input_file = open(path)
    for i in range(int(input_file.readline())):
        (CCount, JCount) = [int(i) for i in input_file.readline().split()]
        CAct = []
        for i in range(CCount):
            CAct.append([int(i) for i in input_file.readline().split()])
        JAct = []
        for i in range(JCount):
            JAct.append([int(i) for i in input_file.readline().split()])
        out.append(TestCase(CAct, JAct))
    input_file.close()
    return out


def solve(path):
    tcs = loadTestCases("B", path)
    output_file = open(path[:-3]+".out", "w")
    count = 1
    for t in tcs:
        output_file.write("Case #"+str(count)+": "+str(t.solve())+"\n")
        print(("Case ________________________________________#"+str(count)))
        count += 1
        
    output_file.close()

        
        
solve("B-large.in")

    
