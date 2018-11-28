#fin = open('cookie.in','r')
fin = open('B-large.in','r')
fout = open('cookie.out','w')

cases = int(fin.readline().strip())

a = 1

def timeToCookie(cookies,goal,rate):
    return (goal-cookies)/rate

def sumList(lst):
    s = 0.0

    for x in lst:
        s += x

    return s

while a <= cases:
    params = fin.readline().strip().split(' ')

    currentRate = 2.0
    currentCookies = 0.0
    

    cost = float(params[0])
    farmRate = float(params[1])
    target = float(params[2])

    times = []

    
    timeToFarm = timeToCookie(currentCookies,cost,currentRate)
    timeWithFarm = timeToCookie(currentCookies,target,currentRate+farmRate)
    totalFarmTime = timeToFarm + timeWithFarm
    timeWOFarm = timeToCookie(currentCookies,target,currentRate)


    while totalFarmTime < timeWOFarm:
        currentRate += farmRate
        times.append(timeToFarm)

        timeToFarm = timeToCookie(currentCookies,cost,currentRate)
        timeWithFarm = timeToCookie(currentCookies,target,currentRate+farmRate)
        totalFarmTime = timeToFarm + timeWithFarm
        timeWOFarm = timeToCookie(currentCookies,target,currentRate)
    
    times.append(timeWOFarm)

    print('Case #'+str(a)+': '+str(sumList(times)))

    a+=1
        

    
