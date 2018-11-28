import sys

with open(sys.argv[1], 'r') as inputFile, open('B-large.out', 'w') as outputFile:
    numTests = inputFile.readline()
    numTests = int(numTests.strip("\n"))
    for i in range(numTests):
        s = inputFile.readline().strip("\n")
        greatestTidyNumber = s
        for j in range(1, len(s)):
            if(int(s[j]) < int(s[j-1])):
                pivotPoint = 0
                for k in range(j-1, 0, -1):
                    if(int(s[k]) > int(s[k-1])):
                         pivotPoint = k
                         break
                greatestTidyNumber = "{}{}{}".format(greatestTidyNumber[:pivotPoint], 
                    str(int(s[pivotPoint]) - 1), "9"*(len(s) - pivotPoint - 1))
                break
        outputFile.write("Case #{}: {}\n".format(i+1, greatestTidyNumber.lstrip("0")))