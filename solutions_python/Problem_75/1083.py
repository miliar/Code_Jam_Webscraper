'''
Created on May 6, 2011

@author: kizzle
'''

def readFromFile(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def parseLine(line):
    d = {}
    numSteps = None
    steps = []
    combs = []
    ops = []
    numCombs = None
    combsDone = 0
    numOps = None
    opsDone = 0
    
    tempString = ""
    tempCounter = 0
    temp = []
    for c in line:
        
        #if c == " ": continue
        if numCombs == None:
            try: 
                int(c)
                tempString += c
            except:
                numCombs = int(tempString)
                tempString = ""
            else:
                continue
        elif combsDone<numCombs:
            temp.append(c)
            if temp.__len__()==3: 
                combs.append(temp)
                temp2 = [temp[1],temp[0],temp[2]]
                combs.append(temp2)
                temp = []
                combsDone+=1
            continue
        elif numOps == None:
            try: 
                int(c)
                tempString += c
            except:
                if tempString == "": continue
                numOps = int(tempString)
                tempString = ""
            else:
                continue
        elif opsDone<numOps:
            temp.append(c)
            if temp.__len__()==2: 
                ops.append(temp)
                temp = []
                opsDone+=1
            continue
        elif numSteps == None:
            try: 
                int(c)
                tempString += c
            except:
                if tempString == "": continue
                
                numSteps = int(tempString)
                tempString = ""
            else: continue
        else: steps.append(c)
    d['steps'] = steps
    d['combs'] = combs
    d['ops'] = ops
    
    return d
    
    
def main():
    #parseLine("2 QRI TWF 3 ZD FQ LK 4 RRQR")
    case = 0
    input = '/home/kizzle/Dropbox/workspace/CodeJamQualifier/input.txt'
    lines = readFromFile(input)
    
    numCases = lines.__len__()-1

    for case in range(numCases):
        result = []
        case +=1
        d = parseLine(lines[case])
        steps = d['steps']
        combs = d['combs']
        ops = d['ops']
        
        for s in steps:
            if s == '\n': continue
            if s == " ": continue
            result.append(s)
            for c in combs:
                if result.__len__()<2: break
                elif result[result.__len__()-1] ==c[0]:
                    if  result[result.__len__()-2] == c[1]:
                        result.pop()
                        result.pop()
                        result.append(c[2])
            for o in ops:
                breakMe = False
                firstSeen = False
                lastSeen = False
                index1 = None
                index2 = None
                counter = -1
                for r in result:
                    counter +=1
                    if r == o[0]: 
                        firstSeen = True
                        index1 = counter
                    elif r == o[1]: 
                        lastSeen = True
                        index2 = counter
                    if firstSeen and lastSeen:
                        result = []
                        breakMe = True
                        break
                if breakMe: break
        outputLine = "Case #" + str(case) + ": ["
        
        lameCounter = 0
        for r in result:
            lameCounter+=1
            outputLine += r
            if lameCounter != result.__len__(): outputLine += ', '
        outputLine += ']'
        print outputLine
    
if __name__ == "__main__": main()