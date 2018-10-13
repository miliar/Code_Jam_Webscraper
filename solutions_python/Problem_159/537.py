
def solve(N, intervals):

    #find max dif
    max = 0

    trick = 0

    old = 0
    for i in range(0,len(intervals)):

        new = old - intervals[i]

        trick += new if new > 0 else 0

        if max < new:
            max = new

        old = intervals[i]

    rythm = max

    #acum at that rythm
    plate = 0
    eat = 0
    for i in range(0,len(intervals)):
        eat += min(rythm,plate)
        plate = intervals[i]

    return trick,eat

if __name__ == '__main__':

    input = open('A-large.in','r')
    output = open('solutionA.txt','w')

    nCases = int(input.readline())

    outList = []

    for case in range(0,nCases):

        N = int(input.readline())
        parts = input.readline().strip().split()

        counts = []
        for i in range(0,len(parts)):

            counts.append(int(parts[i]))

        solution_a, solution_b = solve(N,counts)

        out ='Case #%d: %d %d' % ((case+1),solution_a, solution_b)
        outList.append(out)

    output.write('\n'.join(outList))
    input.close()
    output.close()