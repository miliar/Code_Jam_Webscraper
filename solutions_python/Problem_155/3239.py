

#MAIN
data = open("A-large.in","r").readlines()
print data

output = open("output.txt","w")

test_cases = int(data[0])

#output.write("Output\n")


for i in range(1,test_cases+1):
    case = data[i].split()
    SMAX = int(case[0])
    audience = [int(char) for char in case[1]]
    #print SMAX
    #print audience

    #create an empty array of size SMAX
    friends = [0 for j in range(len(audience))]

    #initialize the count of the zeroth index as 1 if it is zero
    if audience[0] == 0:
        friends[0] = 1;

    #print friends

    currCount = 0
    
    for k in range(0,len(audience)):
        currCount += audience[k]
        if audience[k] >= SMAX or sum(friends) >= SMAX or currCount >= SMAX:
            #print "standing ovation, writing data to file"
            output.write("Case #"+str(i)+": "+str(sum(friends))+"\n")
            #print "Case #"+str(i)+": "+str(sum(friends))+"\n"
            break
            
        elif audience[k] == 0 and currCount <= k:
            friends[k] = 1
            currCount += friends[k]

        
        #print "k=",k,", ",currCount, "friends = ",friends
        
        
output.close()
