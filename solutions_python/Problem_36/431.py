import sys

def findRecursive(text, pattern, position):
    if position == len(pattern):
        return 1
    else:
        count = 0
        for i in range(0, len(text)):
            if(text[i] == pattern[position]):
                count += findRecursive(text[i:], pattern, position + 1)
        return count
                

fh = open(sys.argv[1], "r")
output = open("output.txt", "w")
lines = fh.readlines()
count = lines[0]
pattern = "welcome to code jam"
for i in range(0, int(count)):
    countLine = str(findRecursive(lines[1+i], pattern, 0))
    while(len(countLine) < 4):
        countLine = "0" + countLine
    output.write("Case #" + str(i+1) + ": " +  countLine + "\n")
        


