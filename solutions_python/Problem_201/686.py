from collections import Counter

def readInput(path):
    cases = []
    with open(path, mode='r') as f:
        numCases = f.readline().strip()
        for line in f:
            cases.append((line.strip().split(' ')[0], line.strip().split(' ')[1]))

    return numCases, cases

def printSolutions(solutions, name):
    with open(name, mode='w') as f:
        case = 0
        for solution in solutions:
            case+=1
            f.writelines("Case #"+str(case)+": "+solution+"\n")

def solve(intervals, guests):
    numIntervals=sum(intervals.values())


    if guests>numIntervals:#One guest will fit in each interval
        newIntervals = Counter()
        for intervalSize in intervals:
            quantity = intervals[intervalSize]
            intervals[intervalSize]=0
            if intervalSize%2==1:
                newIntervals[(intervalSize-1)//2]+=quantity*2
            else:
                newIntervals[intervalSize//2]+=quantity
                newIntervals[intervalSize//2-1]+=quantity

        intervals = intervals + newIntervals
        #print(str(intervals)+"---"+str(guests-numIntervals))
        return solve(intervals, guests-numIntervals)
    else:
        #print("SOLVING!" + str(guests))
        IntervalSizes=[key for key in intervals]
        IntervalSizes.sort(reverse=True)
        if intervals[IntervalSizes[0]]>=guests:
            finalInterval = IntervalSizes[0]
        else:
            #if(intervals[IntervalSizes[0]]+intervals[IntervalSizes[1]]<guests):
        #        print("ERROR")
            finalInterval = IntervalSizes[1]

        if finalInterval%2==1:
            return((finalInterval-1)//2,(finalInterval-1)//2)
        else:
            return((finalInterval)//2,(finalInterval)//2-1)


numcases, cases = readInput("Input")
solution = []
for stalls, guests in cases:
    left, right = solve(Counter({int(stalls):1}),int(guests))
    solution.append(str(left) + " " + str(right))

printSolutions(solution, "Output")
