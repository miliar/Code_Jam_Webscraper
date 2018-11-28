import re, itertools, math

input = open('C:\\Users\\Adam\\Downloads\\C-large-1.in', 'r')
#input = open('C:\\Python27\\CodeJam\\Qualification 2013\\inputs.txt', 'r')
output = open('C:\\Python27\\CodeJam\\Qualification 2013\\outputs.out', 'w')

cases = int(input.readline())
case = 1

fairandsquare = []
fairs = []
fairssquared = []

n = int(math.sqrt(1000000000000000))

def ispal(n):
    i = 0
    j = len(n) - 1
    while i < j:
        if n[i] == n[j]:
            i = i + 1
            j = j - 1
        else:
            return False
    return True

for i in range(n):
    if ispal(str(i)):
        fairs.append(i)

for i in fairs:
    fairssquared.append(str(i * i))

for n in fairssquared:
    if ispal(n):
        fairandsquare.append(int(n))

FNS = set(fairandsquare)

while case <= cases:
    x = input.readline().split(' ')
    x[-1] = x[-1].replace('\n', '')
    A = int(x[0])
    B = int(x[1])
    result = 0
    for i in fairandsquare:
        if i >= A and i <= B:
            result = result + 1
    result = "Case #" + str(case) + ": " + str(result)
    if case != cases:
        result = result + "\n"
    output.write(result)
    case += 1
output.close()
input.close()
            
