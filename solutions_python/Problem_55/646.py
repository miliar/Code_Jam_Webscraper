import csv
import collections #Quick queue handling

def readFile(fileName="coaster.dat"):
    fileReader = csv.reader(open(fileName),delimiter=" ")

    #Find amount of input
    inLines = int(fileReader.next()[0])
    outFile = open("coaster.out","w")
    
    for idx in range(inLines):
        ln1 = fileReader.next()
        ln2 = fileReader.next()
        RKN = [int(x) for x in ln1]
        groups = collections.deque([int(x) for x in ln2])
        out= run(RKN,groups)
        outStr = "Case #%s: %s" %(idx+1,out) #Add one for Formatting
        outFile.write("%s\n" %outStr)
        print outStr

    outFile.close()


def run(RKN,groups):
    """Run the rolercoster sim
    @param RKN: 1st line of input file as list
    @param groups: Groups as Deque
    """
    #Init Everythin
    print RKN
    R,k,N = RKN
    totalMoney = 0

    #Corner Case 1 (No one wants to ride today)
    if N == 0:
        return 0
    #Corner Case 2, We have less people than there are seats on the ride (PPL * Rides)
    idx = 0
    totPpl = 0
    while idx < len(groups):
        totPpl += groups[idx]
        if totPpl > k:
            break
        idx += 1

    print "Total People",totPpl, "  ",k
    if totPpl <= k:
        print "LESS PEOPLE THAN SEATS"
        return totPpl * R

    #Otherwise do the main block of the Program
    for ride in range(R):
        #print "Ride %s" %ride
        totalPeople = 0 #How many people are on the coaster
        tempQueue = [] #Groups on the Coaster
        while True:
            #We may run out of groups so
            try:
                nextGroup = groups[0]
            except:
                print "Out of groups"
                break
            
            if totalPeople + nextGroup <= k: # If they fit on
                totalPeople += nextGroup
                tempQueue.append(groups.popleft())
            else:
                break
        #print "On Ride %s  New Queue %s" %(tempQueue,groups)
        totalMoney += totalPeople
        groups.extend(tempQueue)
        #print "New Queue %s" %groups
        #print "Total Money ",totalMoney
    return totalMoney  
    
if __name__ == "__main__":

    readFile("C-small-attempt0.in")
    #RKN = [4, 6, 4]
    #groups = collections.deque([1, 4, 2, 1])
    #print run(RKN,groups)
