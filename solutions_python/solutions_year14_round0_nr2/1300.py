import sys
sys.setrecursionlimit(5000)
global cost, rate, x

'''
def s(corRate,t):
    if (corRate >= x):
        print 
        return t
    else:
        #time to get next upgrade
        time = cost / corRate
        
        #time to get next upgrade + next level
        time += s(corRate + rate, time)
        
        never = x/corRate
        return min(never,  time )

                    
def s(corRate,t):
    if (corRate >= 1500):
        return t
    else:
       return min(x / corRate, cost / corRate + s(corRate + rate, cost / corRate))

'''
def s ():
    corRate = 2
    time = 0
    count = 0
    a , b= {}, {}
    #a = totalTime to get this rate
    a[count] = 0
    # b= totalTime to finish without from this update
    b[count] = x/corRate 
  
    while (True):

        count+=1
        a[count] = a[count-1] + cost/corRate
        corRate+=rate
        b[count] = x/corRate + a[count]
        if (b[count-1] <= b[count]):
            return b[count-1]

        

with open("input.txt","r") as read:
    with open("output.txt", "w") as write:
        total = read.readline()
        total = int(total)
        
        for j in xrange(total):
            cost,rate,x = [float(i) for i in read.readline().split()]
            count = 0 
            write.write("Case #" + str(j+1)+ ": " + "%.7f" %s() + "\n")


