results = []

with open("input.txt") as f:
    inputFile = f.read().splitlines()[1:]

for case, line in enumerate(inputFile):
    shyMax, shyString = line.split()

    #Calculate the extra people required
    standingCount = 0
    extraPeople = 0
    for shyValue, shyValueCount in enumerate(shyString):
        shyValueCount = int(shyValueCount)
        if(shyValueCount > 0):
            extraPeople += max(shyValue - standingCount, 0)
            standingCount += shyValueCount + extraPeople

    results.append("Case #"+str(case+1)+": "+ str(extraPeople))
with open("output.txt", "w") as f:
    f.write("\n".join(results))
