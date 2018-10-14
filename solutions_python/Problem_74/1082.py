'''
Created on May 6, 2011

@author: kizzle
'''
def readFromFile(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def appendToFile(file, lines):
    f = open (file, 'a')
    f.writelines(lines)
    f.close()

def turns(line):
    turns = []
    for c in line:
        if c == "O": turns.append(c)
        elif c == "B": turns.append(c)
    return turns
    
def blue(line):
    expecting = False
    tempString = ""
    blueTurns = []
    for c in line:
        if expecting:
            try: 
                t = int(c)
            except:
                if tempString.__len__() >0:
                    blueTurns.append(int(tempString))
                    tempString = ""
                    expecting = False
            else:
                tempString += c
        if c == "B": expecting = True    
    if tempString.__len__() >0:
        blueTurns.append(int(tempString))
    return blueTurns

def orange(line):
    expecting = False
    tempString = ""
    orangeTurns = []
    for c in line:
        if expecting:
            try: 
                t = int(c)
            except:
                if tempString.__len__() >0:
                    orangeTurns.append(int(tempString))
                    tempString = ""
                    expecting = False
            else:
                tempString += c
        if c == "O": expecting = True
    if tempString.__len__() >0:
        orangeTurns.append(int(tempString))
    return orangeTurns
            
def main():
    
    input = '/home/kizzle/Dropbox/workspace/CodeJamQualifier/trustInput.txt'
    lines = readFromFile(input)
    numCases = lines.__len__()-1
    for case in range(numCases):
        
        case +=1
        count =0
        numPressed =0
        bluePressed = 0
        orangePressed =0
        
       
        
        bluePos = 1
        orangePos = 1
        
        line = lines[case]
        numButtons = int(line[0][0])
        
        turnOrder = turns(line)
        
        blueButtons = blue(line)
        orangeButtons = orange(line)
        
        while numPressed < turnOrder.__len__():
            increment = False
            if bluePressed< blueButtons.__len__():
                if bluePos< blueButtons[bluePressed]: bluePos +=1
                elif bluePos > blueButtons[bluePressed]: bluePos -=1
                elif bluePos == blueButtons[bluePressed]:
                    if turnOrder[numPressed] == "B":
                        increment = True
                        bluePressed +=1
            if orangePressed< orangeButtons.__len__():
                if orangePos< orangeButtons[orangePressed]: orangePos +=1
                elif orangePos > orangeButtons[orangePressed]: orangePos -=1
                elif orangePos == orangeButtons[orangePressed]:
                    if turnOrder[numPressed] == "O":
                        orangePressed +=1
                        numPressed+=1
            if increment: numPressed +=1
            count +=1
        
        print "Case #%d: %d"%(case,count)
if __name__ == "__main__": main()