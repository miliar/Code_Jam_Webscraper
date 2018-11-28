import math

output = open('output.txt','w')

inputFile = open('input.txt','r')
N = int(inputFile.readline())
for i in range(N):
    inp = inputFile.readline().split(" ")
    r = int(inp[0])
    t = int(inp[1])
    a = 2*r-1
    res = int(math.floor((-a+math.sqrt(a*a+8*t))/4))
    print("Case #" + str(i+1) + ": " + str(res))
