# Google Code Jam
inputFile = open('A-large.in', 'r')
outFile = open('small.out', 'w')

# Number of test cases
T = int(inputFile.readline())

# Read in each row
for counter in range(T):
    line = inputFile.readline().split()

    # Max shyness
    SMax = int(line[0])

    # Each of the shyness levels
    audience = list(map(int, list(line[1])))

    # Calculate friends needed to invite
    friends = 0
    totalStanding = 0
    for i in range(SMax+1):
        # If there aren't enough standing, add friends
        if totalStanding < i:
            friends += (i - totalStanding)
            totalStanding = i

        # People at i shyness now stand
        totalStanding += audience[i]

    outFile.write("Case #" + str(counter+1) + ": " + str(friends) + "\n")

outFile.close()
