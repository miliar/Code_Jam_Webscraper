f = open("B-large.in", "rt")

cases = int(f.readline())
output = ""

for x in range(cases):
    case = x+1

    line = f.readline().strip("\n").split(" ")
    
    googlers = int(line[0])
    surpriseTrips = int(line[1])
    minScore = int(line[2])

    numberOfGoodDancers = 0

    minScoreVal = minScore + 2 * (minScore-1)

    minSurpriseVal = minScore + 2 * (minScore-2)

    
    for y in range(googlers):
        score = int(line[y+3])
        if score < minScore:
            continue
        elif score >= minScoreVal:
            numberOfGoodDancers += 1
        elif surpriseTrips > 0 and score >= minSurpriseVal:
            numberOfGoodDancers += 1
            surpriseTrips -= 1
                
    output += str.format("Case #{0}: {1}\n",case,numberOfGoodDancers)

f.close()
f = open("B-large.out", "wt")
f.write(output)
f.close()
