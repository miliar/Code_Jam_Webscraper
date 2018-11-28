__author__ = 'pauful'

file = open('A-large.in', 'r')
solution = open('solution.txt', "w")
numexercises = file.readline()
for line in range(0, int(numexercises)):
    peopleNeeded = 0
    totalPeople = 0
    exer = file.readline().replace("\n", "").split(" ")
    #print exer
    for i in range(0,int(exer[0])+1):

        if int(exer[1][i]) > 0 and (totalPeople + peopleNeeded) < i:
            peopleNeeded += (i - (totalPeople + peopleNeeded))
        totalPeople += int(exer[1][i])
        #print "Total: " +str(totalPeople) + " Shynes: " + str(i) + " People: "+ str(exer[1][i])  +" Needed: " + str(peopleNeeded)
    #print "Case #"+str(line+1) +": "+str(peopleNeeded)
    solution.write("Case #"+str(line+1) +": "+str(peopleNeeded) + "\n")
file.close()
solution.close()