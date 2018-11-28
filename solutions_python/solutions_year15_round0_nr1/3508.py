
filename = "small.in"
#filename = "standingOvation.txt"
f = open('small.out', 'w')

with open(filename, 'r') as text:
    numTests = text.readline()
    caseNum = 1
    #print(numTests)
    for line in text:
        linePos = 0
        peopleStanding = 0
        friendsNeeded = 0
        for index, num in enumerate(line.strip()):

            if(linePos > 1):
                #print("num",num);
                #print("index",(index-2))
                if(num=='0'):
                    print('skip')
                    continue;
                
                if((index-2) > peopleStanding):
                    friendsNeeded = friendsNeeded + ((index-2)-peopleStanding)
                    print("friends needed", friendsNeeded);
                    peopleStanding = peopleStanding + ((index-2)-peopleStanding) + (int(num))
                else:
                    peopleStanding = peopleStanding + int(num)
                #print("people standing",peopleStanding,"\n")
                
            linePos = linePos + 1
        #print("Case #",caseNum, ": ",friendsNeeded,"\n\n")
        f.write("Case #"+str(caseNum)+": "+str(friendsNeeded)+'\n')
        caseNum = caseNum + 1

f.close();
