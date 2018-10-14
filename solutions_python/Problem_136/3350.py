import math
files = open('B-small-attempt0.in', 'r')

T = int(files.readline())

for x in xrange(0,T):
    a = files.readline().split(' ')
    a = [a[0],a[1],a[2].split('\n')[0]]
    a = map(float,a)
    
    costFarm = a[0] #c
    farmIncr = a[1] #f
    goalVal = a[2]  #x
    
    optimal = False
    com = []
    
    goalFarms = 0.0
    numFarms = 0.0
    val = 0.0
    time = 0.0
    
    while(optimal == False):
        while(goalVal > val):
            if (goalFarms > numFarms):
                time = time + costFarm/( 2.0 + (farmIncr*numFarms) )
                val = 0.0
                numFarms = numFarms + 1
            else:
                time = time + (goalVal-val)/(( 2.0 + (farmIncr*numFarms) ))
                val = goalVal
        com.append(time)
        
        val = 0.0
        goalFarms = goalFarms + 1.0
        numFarms = 0.0
        time = 0.0
        
        if len(com) >= 2:
            if (com[len(com)-2] <= com[len(com)-1]):
                optimal = True
                v = math.ceil(com[len(com)-2]*10000000)/10000000
                print("Case #" +str(x+1)+ ": " + str(v))