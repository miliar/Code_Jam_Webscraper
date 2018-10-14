import math

class FastCalculator(object):

    @staticmethod
    def GetPeriodAndOffset(people):
        period = 2**(int(math.log(people, 2)) + 1)
        offset = period//2
        return period, offset

    @staticmethod
    def Calculate(stalls, people):

        period, offset = FastCalculator.GetPeriodAndOffset(people)

        otherMin = (stalls-people) // period
        otherMax =  (((stalls-people) % period) + offset) // period + otherMin

        return otherMax, otherMin

        max = PeriodicValueIncreaser(period, offset)
        min = PeriodicValueIncreaser(period, 0)

        for i in range(people, stalls):
            max.IncreaseOne()
            min.IncreaseOne()

        return max.value, min.value

def solver():
    output = []

    casesToSolve = int(input())
    for i in range(1, casesToSolve+1):
        stalls, people = input().split(' ')
        result = FastCalculator.Calculate(int(stalls), int(people))
        output.append('Case #%s: %s %s' % ((i, ) + result))

    print('\n'.join(output))


solver()
