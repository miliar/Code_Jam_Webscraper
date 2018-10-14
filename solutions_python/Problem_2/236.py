import bisect
filename = 'TrainTimetable-large'
input = open(filename + '.in',  'r')
output = open(filename + '.out',  'w')
cases = int(input.readline().rstrip())
for i in xrange(1, cases+1 ):
    turn = int(input.readline().rstrip())
    noA,  noB = [int(x) for x in input.readline().rstrip().split()]
    demandA = []
    supplyB = []
    for j in xrange(noA):
        times = [int(x.split(':')[0])*60+int(x.split(':')[1]) for x in input.readline().rstrip().split()]
        bisect.insort_left(demandA,  times[0])
        bisect.insort_left(supplyB,  times[1])
    supplyA = []
    demandB = []
    for j in xrange(noB):
        times = [int(x.split(':')[0])*60+int(x.split(':')[1]) for x in input.readline().rstrip().split()]
        bisect.insort_left(demandB,  times[0])
        bisect.insort_left(supplyA,  times[1])
    startA = len(demandA)
    startB = len(demandB)
    for d in demandA:
        for s in supplyA:
            if d >= s+turn:
                startA -= 1
                supplyA.remove(s)
                break
    for d in demandB:
        for s in supplyB:
            if d >= s+turn:
                startB -= 1
                supplyB.remove(s)
                break
    output.write('Case #' + str(i) + ': ' + str(startA if startA >= 0 else 0) + ' ' + str(startB if startB >= 0 else 0) + '\n')
input.close()
output.close()
