import math

input = open("lm.in" , "r")
output = open("lm.out" , "w")
cases = int(input.readline())

for i in range(1, cases + 1):
    result = "YES"
    [m, n] = [int(x) for x in input.readline().split()]
    lawn = []
    for j in range(0, m):
        lawn.append([int(y) for y in input.readline().split()])
    tlawn = map(list, zip(*lawn))

    for k in range(0, m):
        for l in range(0, n):
            if lawn[k][l] != max(lawn[k]) and lawn[k][l] != max(tlawn[l]):
                result = "NO"
    print "Case #" + str(i) + ": " + result
    output.write("Case #" + str(i) + ": " + result + "\n")
input.close()
output.close()
