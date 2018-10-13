#!/usr/bin/python
import sys
import scipy

def prepareTable(g, k):
    """
    generating the trip tables with the income per ride and the number of included groups
    """
    N = len(g)
    distance = scipy.ones(scipy.shape(g))
    tempsize = g.copy()
    finalsize = g.copy()
    i = 1
    while not scipy.all(tempsize>k) and i < N:
        tempsize += scipy.concatenate((g[i%N:],g[:i%N]))
        pos = scipy.where(tempsize<=k)
        distance[pos] += 1
        i+=1
        finalsize[pos] = tempsize[pos]

    return distance, finalsize

    
def getIncome(R, N, params):
    distance, ridesize = params


    """
    try to figure out the periodicity and the number of steps until periodic state is reached
    """
    perincome = 0L
    i = 0
    position = [0,]
    income = [0,]
    while position.count(i)<2:
        perincome += ridesize[i%N]
        i = (i + distance[i%N]) % N
        position.append(i)
        income.append(perincome)


    offset = position.index(i)
    offsetincome = income[offset]

    period = len(position[offset+1:])
    perincome = income[-1] - income[offset]
    

    if R < offset:
        return income[R]

    else:
        """
        make the last few steps < period
        """
        addincome = 0L
        for steps in range((R-offset)%period):
            addincome += ridesize[i%N]
            i += distance[i%N]

    return offsetincome + ((R-offset) / period) * perincome + addincome


def main():
    data = sys.stdin.readlines()[1:]

    case = 0
    while 1:
        case += 1
        try:
            line1 = data.pop(0)
            line2 = data.pop(0)
        except:
            sys.exit(0)
        R, k, N = map(long, line1.split(' '))
        g = scipy.array(map(long, line2.split(' ')))

        params = prepareTable(g, k)

        income = getIncome(R,N, params)
        
                   
        print "Case #"+str(case)+": "+str(income)
             

if __name__ == '__main__':
    main()
