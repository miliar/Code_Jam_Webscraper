import sys


#bruteforce
def solve(values):
    xor0 = 0
    for x in values:
        xor0 = xor0 ^ x
    if (xor0 != 0):
        return 'NO'
    
    result = 0
    for i in range(1, pow(2, len(values))/2):
        xor1 = 0
        xor2 = 0
        sum1 = 0
        sum2 = 0
        temp = i
        for j in range(0,len(values)):
            if (temp & 1 == 1):
                xor1 = xor1 ^ values[j]
                sum1 = sum1 + values[j]
            else:
                xor2 = xor2 ^ values[j]
                sum2 = sum2 + values[j]
            temp = temp >> 1
        if (xor1 == xor2):
            result = max(sum1, sum2, result)
    return result


#some nasty IO stuff...
#the input file is assumed to end with .in
filename = sys.argv[1]
input = open(filename, 'r')
output = open(filename[:-2] + 'out', 'w')
lines = iter(input)
T = int(lines.next()) #read in the number of test cases
i = 1
for line in lines:
    values = map(int, lines.next().split(" "))
    output.write('Case #' + str(i) + ': ' + str(solve(values)))
    if (T!=i):
        output.write('\n')
    i = i + 1
input.close
output.close