infile = open('data/C-small-attempt2.in.in','r')
outfile = open('output/C-small-attempt2.out', 'w')

data = infile.readlines()
data = [item.strip().split() for item in data]
test_cases = int(data[0][0])
data = data[1:]

answers = []

for case in range(test_cases):
    money = 0
    params = data[case * 2]
    groups = data[case * 2 + 1]
    groups = [int(item) for item in groups]
    rides = int(params[0])
    capacity = int(params[1])
    nogroups = int(params[2])
    i = 0
    for ride in range(rides):
        riders = 0
        lasti = -1
        while True:
            if riders + groups[i % nogroups] <= capacity and i % nogroups != lasti:
                riders += groups[i % nogroups]
                if lasti == -1:
                    lasti = i % nogroups
                i += 1
            else:
                break
        money += riders
    answers.append(money)
            
for i in range(test_cases):
    str = 'Case #%d: %s\n' % (i+1, answers[i])
    outfile.write(str)

infile.close()
outfile.close()

