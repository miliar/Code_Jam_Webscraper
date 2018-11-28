def main():
    fileInput = open("A-large.in",'r')
    lines = fileInput.readlines()
    T = int(lines[0].strip())
    output = ""
    for x in xrange(T):
        lineArray = lines[x+1].strip().split()
        sMax = int(lineArray[0])
        peopleNum = 0
        inviteFriends = 0
        if sMax == 0:
            inviteFriends = 0
            output += "Case #" + str(x+1) + ": " + str(inviteFriends) + '\n'
        else:
            for currentShyness in xrange(sMax+1):
                if currentShyness <= peopleNum:
                    peopleNum += int(lineArray[1][currentShyness])
                elif lineArray[1][currentShyness] > 0:
                    inviteFriends += currentShyness - peopleNum
                    peopleNum += currentShyness - peopleNum
                    peopleNum += int(lineArray[1][currentShyness])
                    
            output += "Case #" + str(x+1) + ": " + str(inviteFriends) + '\n'

    fileOutput = open("output.in",'w')
    fileOutput.write(output)

main();
                
            
        
    
        
	
