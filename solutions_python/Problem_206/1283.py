def find_slowest(destination, runners):
    road_left = [destination - run[0] for run in runners]
    time_to = []
    for i in range(len(runners)):
        time_to.append(float(road_left[i])/runners[i][1])
    return max(time_to)

def solve(infd, outfd, rang):
    line = infd.readline()
    destiny, N = line.split()
    destiny = float(destiny)
    N = int(N)
    runners = []
    for i in range(N):
        initpos, speed = infd.readline().split()
        initpos = int(initpos)
        speed = int(speed)
        runners.append((initpos,speed))
    time = find_slowest(destiny,runners)
    speed = destiny/time

    output = "Case #%i: %.6f \n" % (rang,speed)
    outfd.write(output)
