
inputfile = "C-small-attempt1.txt"
resultfile = "rollerSmallOut.txt"

infile = open(inputfile, "r")
x = 0
y = 0

y = int (infile.readline() )
print("n cases = ", y)

while infile and x<y:
    x+=1
    line = infile.readline()
    stuff = line.split();
    r = int (stuff[0] )
    k = int (stuff[1] )
    n = int (stuff[2] )
    line = infile.readline() #get second line of case
    groupsStrings = line.split()
    groups = [int(i) for i in groupsStrings]
    #print(groups)
    nEuros = 0;
    nRuns = 0;
    #do work
    while (nRuns < r):
        nPassengers = 0;
        passengers = []
        while (groups != [] and groups[0] + nPassengers <= k):
                thisgroup = groups.pop(0);
                nPassengers += thisgroup;
                passengers.append(thisgroup)

        groups.extend(passengers)

        nEuros += nPassengers;
        nRuns+=1;

    #what's the size of an integer in python for everflow checks

    print ("Case #{0}: {1}".format(x, nEuros))
 
        
