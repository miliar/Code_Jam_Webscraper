#!python3
import fileinput

if __name__ == "__main__":
    aFile = fileinput.input("A-small-attempt0.in")
    aNbOfCases = aFile.readline()
    outputFile = open("result.out", 'w')
    for i in range(int(aNbOfCases)):
        outputFile.write("Case #"+str(i+1)+": ")
        aLine = aFile.readline()
        aMaxShyness = int(aLine[:2])
        aAudience= map(int, list(aLine[2:-1]))
        aNbOfClappingMembers = 0
        aNbOfFriendsNeeded = 0
        for aCurrentShyness in range(0, aMaxShyness+1):
            if(not aAudience[aCurrentShyness]):
                #check if chain will break here (needing friends) or not
                if(aNbOfClappingMembers < aCurrentShyness+1):
                    aNbOfFriendsNeeded += 1
                    aNbOfClappingMembers += 1
            else:
                aNbOfClappingMembers += aAudience[aCurrentShyness]
        outputFile.write(str(aNbOfFriendsNeeded)+"\n") 
    outputFile.close()
