import fractions
import math
def casePrint(i, result):
    writer.write('Case #'+str(i)+': '+result+'\n')




inputFile = 'd:/B-small.in'
outputFile = 'd:/B-small.out'
reader = open(inputFile, 'r')
writer = open(outputFile, 'w')

numCases = int(reader.readline())

for i in range(1, numCases+1):
    tokens = reader.readline().strip().split(' ')
    numEvent = int(tokens[0])
    events = tokens[1:]
    maxvalue = 0
    for j in range(0, numEvent):
        events[j] = int(events[j])
        maxvalue = max(maxvalue, events[j])

    gcdvalue = 0
    for first in range(0, numEvent):
        for second in range(0, numEvent):
            if events[first] != events[second]:
                difference = abs(events[first] - events[second])
                if difference != 0:
                    if gcdvalue == 0:
                        gcdvalue = difference
                    else:
                        gcdvalue = fractions.gcd(gcdvalue, difference)
    future = math.ceil(maxvalue/gcdvalue) * gcdvalue
    result = future - maxvalue
    if result < 0:
        result += gcdvalue;
    casePrint(i, str(result))
                


reader.close();
writer.close();


