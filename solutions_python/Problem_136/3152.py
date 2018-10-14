txtlist = [i.strip() for i in open('input2.txt').readlines()]
output = open('cookieout2.txt','w')
numOfCases = int(txtlist[0])

def cookiesolver(cost,farm,originalgoal):
    rate = 2.0
    timeWithoutFarm = originalgoal/2.0
    newgoal = timeWithoutFarm    
    goal = float('inf')    
    numOfFarms= 0.0    
    farmrate =  cost/rate
    while newgoal < goal:
        goal = newgoal
        numOfFarms +=1
        newproduction = farm*numOfFarms + 2 
        newgoal = originalgoal/newproduction + farmrate
        farmrate += cost/newproduction
    return goal
        

for i in range(numOfCases):
    c,f,x = txtlist[i+1].split()
    outstring = str(cookiesolver(float(c),float(f),float(x)))
    output.write('Case #'+ str(i+1)+': '+outstring+'\n')
