def findcard():
    f = open("/Users/zulsarbatmunkh/Downloads/B-small-attempt0.in.txt")
    Input = f.read()
    f.close()
    rows = Input.split("\n")
    testcases = int(rows[0])
    answer = ""
    i=1
    while i<testcases+1:
        farmcost = float(rows[i].split()[0])
        farmrate = float(rows[i].split()[1])
        goal = float(rows[i].split()[2])
        value = findTime(farmcost, farmrate, goal)
        answer += "Case #" + str(i) + ": " + str(value)+"\n"
        i+=1
    return answer[:-1]

def findTime(farmcost, farmrate, goal):
    start = 0
    rate = 2.0
    farms = 0
    time = 0
    while goal / rate > farmcost/rate + goal/(rate+farmrate):
        time+=farmcost/rate
        rate+=farmrate
        farms+=1
    time += goal/rate
    return time
    

print findcard()
