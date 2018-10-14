import sys
import string

f = open(sys.argv[1],'r')
t = int(f.readline())
for i in xrange(t):
    combiners = {}
    opposers = {}
    line = f.readline().split()
    c = int(line[0])
    last = 0
    for index in xrange(c):
        combo = line[index+1]
        combiners[combo[0]] = (combo[1],combo[2])
        combiners[combo[1]] = (combo[0],combo[2])
        last += 1
    last += 1
    d = int(line[last])
    for index in xrange(d):
        oppose = line[index+last+1]
        opposers[oppose[0]] = oppose[1]
        opposers[oppose[1]] = oppose[0]
        last += 1
    n = int(line[last+1])
    base = line[last+2]

    result = []
    for char in base:
        if len(result) == 0:
            result.append(char)
        else:
            try:
                if combiners[char][0] == result[-1]:
                    result[-1] = combiners[char][1]
                    notInCombiner = False
                else:
                    notInCombiner = True
            except KeyError:
                notInCombiner = True

            try:
                if notInCombiner and opposers[char] in result:
                    result = []
                    notInOpposer = False
                else:
                    notInOpposer = True
            except KeyError:
                notInOpposer = True

            if notInCombiner and notInOpposer:
                result.append(char)

    answer = "["
    answer += string.join(result,", ")
    answer += "]"
    print "Case #%d: %s" % (i+1,answer)