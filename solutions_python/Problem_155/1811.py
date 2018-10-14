f = open('A-large.in', 'r')

cases = int(f.readline())


for case in range(cases):
    caseInfo = f.readline().split(" ")
    caseInfo[1] = caseInfo[1].rstrip('\n')

    people = str(caseInfo[1])
    totalStanding = 0
    friendsNeeded = 0
    for x in range(len(people)):
        if x == 0:
            totalStanding += int(people[0])
        elif int(people[x]) == 0:
            pass
        else:
            if totalStanding >= x:
                totalStanding += int(people[x])
            else:
                friendsNeeded += (x - totalStanding)
                totalStanding += ((x-totalStanding)+int(people[x]))

    print("Case #"+str(case+1)+": "+str(friendsNeeded))
    
        
