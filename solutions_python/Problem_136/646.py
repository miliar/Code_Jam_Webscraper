import sys

def best_time(cost, marginal, goal, cps):
    time = 0.0
    while ((goal - cost)/cps > goal/(marginal + cps)):
        time += cost/cps
        cps += marginal
    return str(time + goal/cps)

input_file = open(sys.argv[1])
input = []
output = open("output.txt", "w")
for line in input_file:
    input.append(line)
for i in range(1, int(input[0])+1):
    args = input[i].split()
    output.write("Case #" + str(i) + ": " + best_time(float(args[0]),float(args[1]),float(args[2]), 2.0) + "\n")