f = open('C:\\Users\\djspence\\Downloads\\A-large (1).in', 'r')

tries = int(f.readline())

for case in range(0, tries):
    timesToFinish = []
    vals = f.readline().strip().split(' ')
    destination = int(vals[0])
    numHorses = int(vals[1])
    for i in range(0, numHorses):
        vals2 = f.readline().strip().split(' ')
        pos = int(vals2[0])
        speed = int(vals2[1])
        timesToFinish.append(((destination-pos)*1.0)/speed)
    ourTime = max(timesToFinish)
    ourSpeed = (destination*1.0)/ourTime
    print("Case #" + str(case+1)+": " + str(ourSpeed))