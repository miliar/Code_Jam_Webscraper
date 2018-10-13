## Solution for CodeJam "ThemePark" Problem
## By Addison Hardy, hardy.addison@gmail.com

## Create some variables
TestCaseNumber = 0

## Read lines from input file
inputfile = open("C-small-attempt0.in")
inputlines = inputfile.readlines()
inputfile.close()

TestCaseNumber = inputlines[0]
del inputlines[0]

## Process input lines

count = 0
finalcount = 1

solution = []

for case in range(len(inputlines)/2):
    line1 = inputlines[count].split(" ")
    line2 = inputlines[count+1].split(" ")

    groups = []

    for item in line2:
        groups.append(int(item.strip("\n")))

    R = int(line1[0].strip("\n"))
    k = int(line1[1].strip("\n"))
    N = int(line1[2].strip("\n"))

    euros = 0

    for ride in range(R):
        
        ride_k = k
        group_count = 0
        ride_full = 0

        for group in groups:
            if (ride_k - group) > -1:
                if ride_full == 0:
                    ride_k -= group
                    euros += group
                    group_count += 1
            else:
                ride_full = 1

        for ridegroup in range(group_count):
            groups.append(groups[0])
            del groups[0]

    solution.append("Case #"+str(finalcount)+": "+str(euros))
    count += 2
    finalcount += 1

outfile = open("output.out", "w")
for line in solution:
    outfile.write(line+"\n")
outfile.close()

print "Output file written. Operation DONE."
