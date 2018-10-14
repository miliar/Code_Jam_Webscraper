import code

infile = open('data/A-large.in.in','r')
outfile = open('output/A-large.out', 'w')
data = infile.readlines()

data = [item.strip().split() for item in data]
test_cases = int(data[0][0])
data = data[1:]
answers = []

for line in data:
    snappers = int(line[0])
    snaps = int(line[1])
    target = 2**snappers
    if snaps == 0:
        answers.append("OFF")
    elif snaps % target == target - 1:
        answers.append("ON")
    else:
        answers.append("OFF")

for i in range(test_cases):
    str = 'Case #%d: %s\n' % (i+1, answers[i])
    outfile.write(str)

infile.close()
outfile.close()

