def listvalid(list):
    if len(list) < 2:
        return True
    else:
        return list[-1] < list[-2]

def solve(cases, inFile, outputFile):
    for c in xrange(1, cases + 1):
        outputFile.write("Case #" + str(c) + ": ")
        farmcost, rateincr, goal = tuple(map(float, inFile.readline().split()))
        rate = 2
        list = []
        while listvalid(list):
            sum = 0
            sum += goal / rate
            n = rate - rateincr
            while n > 1.99:
                sum += farmcost / n
                n -= rateincr
            rate += rateincr
            print sum
            list.append(sum)
        outputFile.write("%.7f" % list[-2])
        outputFile.write("\n")
        
inFile = open('B-small-attempt2.in')
outputFile = open('output.txt', 'w')

cases = int(inFile.readline())
print cases, 'cases read'

solve(cases, inFile, outputFile)
print 'done'

inFile.close()
outputFile.close()