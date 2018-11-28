__author__ = 'panmari'


answers = []
filename = 'B-large.in'

#initial cookies per second
initial_cps = 2.0
answers = []
with open(filename) as file:
    nr_problems = file.readline()
    while True:
        nextLine = file.readline()
        if nextLine == '':
            break
        l = nextLine.split(' ')
        c = float(l[0]) # cost farm
        f = float(l[1]) # extra cookies/second per farm
        x = float(l[2]) # amount that needs to be achieved

        minimal_time = x/initial_cps
        k = 0
        current_cps = initial_cps
        time = 0
        while True:
            time += c / current_cps # plus time to accomodate one more farm
            current_cps += f
            sprint_time = time + x/current_cps
            if sprint_time > minimal_time:
                break
            else:
                minimal_time = sprint_time
        answers.append(minimal_time)

with open(filename + '.out', 'w') as f:
    for n, answer in enumerate(answers):
        f.write("Case #{}: {}\n".format(n + 1, answer))