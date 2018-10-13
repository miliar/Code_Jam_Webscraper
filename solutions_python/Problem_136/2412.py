def foo(cost, increase, target):
    cps = 2
    bestTime = target/cps
    newTime = bestTime
    wait = 0
    while newTime == bestTime:
        wait += cost/cps #time spent buying farms
        cps += increase
        newTime = wait + target/cps
        if newTime > bestTime:
            break
        bestTime = newTime
    return round(bestTime, 7)



file = open("B-large.in.txt", "r")
output = open("outputLargeB.txt", "w")
for i in range(int(file.readline())):
    C, F, X = [float(n) for n in file.readline().split()]
    output.write("Case #" + str(i+1) + ": " + str(foo(C, F, X)) + "\n")
    


file.close()
output.close()
