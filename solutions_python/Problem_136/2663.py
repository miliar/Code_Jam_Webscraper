def sim(C, F, X, rate):
    y = C/rate
    rate += F
    z = X/rate
    return y + z, y, rate

inputs = open("test.txt")
output = open("output.txt", "w")
noCases = int(inputs.readline())

for i in range(noCases):
    line = inputs.readline()
    line = line.strip().split()
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])
    rate = 2.0
    first = X/rate
    time = 0
    options = [first]
    while time < first:
        
        a, b, rate = sim(C, F, X, rate)
        options.append(a + time)
        time += b
        if len(options) > 1:
            if options[-1] > options[-2]:
                break
    output.write("Case #" + str(i + 1) + ": " + str(min(options)))
    output.write('\n')
output.close()
inputs.close()