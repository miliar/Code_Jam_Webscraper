import math

#inputFile = open("test.txt", "r")
inputFile = open("A-small-attempt1.in","r")
output = open("Round1AAsmall.txt","w")

cases = int(inputFile.readline())

for case in range(1,cases+1):
    r, p = map(int, inputFile.readline().strip().split(" "))
    m = (r + 1) / 2.0
    n = math.floor((0.25 * (math.sqrt(16 * (m ** 2) - 24 * m + 8 * p + 9) - 1))*2) / 2.0
    #print n - m + 1
    output.write("Case #%d: %d" % (case, n - m + 1))
    if case != cases:
        output.write("\n")

inputFile.close()
output.close()