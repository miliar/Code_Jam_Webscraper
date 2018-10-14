import math

f = file("B-large_input.txt", 'r').readlines()
f_output = file("output_large.txt", 'w')
numCases = int(f[0])
currentCase = 0

for case in f[1:]:
    print currentCase
    currentCase+=1
    farmCost, farmRate, target = map(float, case.split(" "))
    times = [target/2.0]
    farmTimes = []
    i = 0
    while True:
        farmTimes.append(farmCost/(2.0+(farmRate*(len(times)-1))))
        currentTime = sum(farmTimes)+(target/(2.0+(farmRate*(len(times)))))
        if times[-1] > currentTime:
            times.append(currentTime)
        else:
            f_output.write("Case #%i: %.7f\n" % (currentCase, times[-1]))
            break
f_output.close()

