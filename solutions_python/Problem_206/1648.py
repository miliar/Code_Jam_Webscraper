t = int(input())  # read a line with a single integer
filep = open("curise.txt", "w")
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    positions = []
    speeds = []
    for j in range(1, m + 1):
        k, s = [int(l) for l in input().split(" ")]
        positions.append(k)
        speeds.append(s)
    nearest = 0
    num = 0
    for a in range(len(positions)):
        if positions[a] > nearest:
            nearest = positions[a]
            num = a
    speed1 = speeds.pop(num)
    position1 = positions.pop(num)
    if m == 1:
        time = (n - position1)/speed1
        result = n/time
    else:
        speed2 = speeds.pop()
        position2 = positions.pop()
        if speed1 >= speed2:
            time = (n - position2)/speed2
            result = n/time
        else:
            meet_time = (position1 - position2)/(speed2 -  speed1)
            after_time = (n - (position2 + speed2 * meet_time))/speed1
            if after_time < 0:
                meet_time = (n - position2)/speed2
                result = n / meet_time
            else:
                result = n / (meet_time + after_time)
    filep.write("Case #{}: {}\n".format(i, result))
filep.close()
