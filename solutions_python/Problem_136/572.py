_ = int(input())
answers = []

for i in range(_):
    time = 0
    cps = 2

    c, f, x = list(map(float, input().split()))
    while True:
        toX = x/cps
        toFarm = c/cps
        toXwithFarm = toFarm + x/(cps+f)
        #print("toX:", str(toX), "\ntoFarm:", str(toFarm), "\ntoXwF:", toXwithFarm)
        if toXwithFarm < toX:
            cps += f
            time += toFarm
        else:
            time += toX
            break
    tap = "Case #" + str(i+1) + ": " + str(time)
    answers.append(tap)

[print(x) for x in answers]
