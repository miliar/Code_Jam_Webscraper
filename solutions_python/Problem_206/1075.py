def calc(horses):
    maxEndTime = 0

    for horse in horses:
        speed = horse[1]
        start = horse[0]
        endTime = (end-start)/speed
        maxEndTime = max(endTime, maxEndTime)

    mySpeed = end/maxEndTime
    return mySpeed

outFile = open("A-large.out", "w")

with open("A-large.in") as f:
    cnt = int(f.readline().split()[0])
    for i in range(cnt):
        split = f.readline().split()
        end = int(split[0])
        horses = []
        for j in range(int(split[1])):
            horses.append(tuple(int(val) for val in f.readline().split()))
        print("Case #" + str(i+1) + ":", calc(horses), file=outFile)

outFile.close()
