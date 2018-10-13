file = open('C:\Documents and Settings\davos\Local Settings\Temp\B-large.in.txt')
global iterations
iterations = int(file.readline())
def getLine():
    temp = file.readline().split()
    return [float(temp[0]),float(temp[1]),float(temp[2])]
    
def time(cost, production, win, x):
    totalTime = 0
    cps = 2
    while x>0:
        x-=1
        totalTime += cost/cps
        cps += production
    totalTime += win/cps
    return totalTime

def time2(cost, production, win):
    cps = 2
    timef = cost/cps
    totalTime = 0
    while (win/cps > timef + win/(cps+production)):
        cps += production
        totalTime += timef
        timef = cost/cps
    totalTime += win/cps
    return totalTime

def test2():
    f = getLine()
    return time2(f[0],f[1],f[2])

def test():
    f = getLine()
    flag = True
    prevCase = time(f[0],f[1],f[2],0)
    currentTest = 1
    while flag:
        thisCase = time(f[0],f[1],f[2],currentTest)
        if prevCase<thisCase:
            flag=False
        elif prevCase>thisCase:
            prevCase = thisCase
        currentTest += 1
    return prevCase

def out():
    global iterations
    output = open('C:\Documents and Settings\davos\Local Settings\Temp\B-large.out','w')
    kwrite = ''
    count = 1
    while iterations!=0:
        iterations -= 1
        print(iterations)
        kwrite = kwrite + 'Case #' + str(count) + ': ' + str(test2()) + '\n'
        count += 1
    output.write(kwrite)
    
