def timeToDest(init, dest, spd):
    return (dest - init) / spd

def spdForTime(init, dest, time):
    return (dest - init) / time

def process(string):
    string = string.split()
    return int(string[0]), int(string[1])

def processHorse(string, dest):
    string = string.split()
    return timeToDest(int(string[0]), dest, int(string[1]))

cases = int(input())
for x in range(cases):
    dest, horseNum = process(input())
    horses = []
    for n in range(horseNum):
        horses.append(processHorse(input(), dest))
    spd = spdForTime(0, dest, max(horses))
    print("Case #{}: {:.6f}".format(x+1, spd))
