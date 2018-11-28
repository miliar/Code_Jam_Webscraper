
def left(numStall, numPeople):
    # print numStall, numPeople

    numStall = numStall - 1
    halfStall = numStall / 2
    numPeople = numPeople - 1
    if numPeople == 0:
        return numStall - halfStall, halfStall

    if numPeople % 2 == 0:
        return left(numStall/2, numPeople/2)

    return left(numStall - numStall/2, numPeople - numPeople/2)

for i in xrange(int(raw_input())):
    answer = left(*(int(arg) for arg in raw_input().split(' ')))
    print "Case #%d: %d %d" % (i+1, answer[0], answer[1])
