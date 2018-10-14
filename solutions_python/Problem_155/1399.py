def addingfunc(SMax, peopleArr):
    standing = 0
    currentS = 0
    missing = 0
    while(currentS<=SMax):
        if standing>=currentS:
            standing = standing + peopleArr[currentS]
            currentS+=1
        else:
            missing+=1
            standing+=1
    return missing


file = open("A-large.in")
lines = file.read().split("\n")
out = open("output", 'w')
first = 0
for case in range(1,int(lines[0])+1):
    if first!=0:
        out.write("\n")
    first+=1
    line = lines[case]
    line = line.split(" ")
    SMax = int(line[0])
    peopleArr = [int(i) for i in line[1]]
    missing = addingfunc(SMax, peopleArr)
    print("Case #" + str(case) + ": " + str(missing))
    out.write("Case #" + str(case) + ": " + str(missing))
out.close()
