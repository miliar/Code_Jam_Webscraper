# Google Code Jam for problem A
prefix = './A/'
inputFile = open(prefix + 'A-large.in', 'r')
outFile = open(prefix + 'out.out', 'w')

# Number of test cases
T = int(inputFile.readline())

# Read in each row
for counter in range(T):

    # Number of mushrooms
    N = int(inputFile.readline())

    # Mushrooms
    M = list(map(int, inputFile.readline().split()))

    # Method 1
    count1 = 0
    greatestDiff = None

    for i in range(1, len(M)):
        diff = M[i] - M[i-1]
        if diff < 0:
            count1 += abs(diff)
        if greatestDiff is None or -diff > greatestDiff:
            greatestDiff = -diff

    # Method 2
    count2 = 0
    if greatestDiff > 0:
        for i in range(N-1):
            if M[i] - M[i+1] < greatestDiff:
                count2 += min(M[i], greatestDiff)
            else:
                count2 += greatestDiff

    outFile.write("Case #" + str(counter+1) + ": " + str(count1) + " " + str(count2) + "\n")

outFile.close()
