import sys


def solve(seq):
    steps = 0
    pos = { 'O' : 1, 'B' : 1}
    last_action = { 'O' : 0, 'B' : 0}
    for (robot, button) in seq:
        steps_needed = abs(button - pos[robot])
        time_since_last_action = steps - last_action[robot]
        steps = steps + max(0, steps_needed - time_since_last_action) + 1
        last_action[robot] = steps
        pos[robot] = button
    return steps


#some nasty IO stuff...
filename = sys.argv[1]
input = open(filename, 'r')
output = open("output/" + filename.split("/")[1], 'w')
lines = iter(input)
T = int(lines.next()) #read in the number of test cases
i = 1
for line in lines:
    seq = line[line.find(" "):].strip().split(" ")
    seq = zip(seq[::2], seq[1::2])
    for j in range(0, len(seq)):
        seq[j] = (seq[j][0], int(seq[j][1]))
    output.write('Case #' + str(i) + ': ' + str(solve(seq)))
    if (T!=i):
        output.write('\n')
    i = i + 1
input.close