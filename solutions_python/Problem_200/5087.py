import sys

def findTidy(number):
    prevN = 0
    for n in str(number):
        n = int(n)
        if(n >= prevN):
            prevN = n
        else:
            return False
    return True

# read file and split into an array of lines
file = sys.stdin.read()
text = file.splitlines()

cases = []
noCases = text[0]

cases = text[1:]
cases = list(map(int, cases))

outStr = ""
for i in cases:
    lastTidy = 0
    for j in range(i + 1):
        if(findTidy(j) and j > lastTidy):
            lastTidy = j
    outStr += "Case #{}: {}\n".format(cases.index(i) + 1, lastTidy)
with open("out.txt", "w") as f:
    f.write(outStr)