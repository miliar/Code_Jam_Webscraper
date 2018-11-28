__author__ = 'Sean'

fin = open('problema-in.txt')
fout = open('problema-out.txt', 'w')

num_cases = int(fin.readline())

for case in range(num_cases):
    rounds = []
    for n in range(2):
        answer = int(fin.readline())
        lines = []
        for i in range(4):
            line = fin.readline().split()
            line = [int(i) for i in line]
            lines.append(line)
        rounds.append(lines[answer-1])
    out = (set(rounds[0]).intersection(rounds[1]))
    if len(out) == 1:
        fout.write("Case #" + str(case+1) +": " + str(out.pop()) + "\n")
    elif len(out) > 1:
        fout.write("Case #" + str(case+1) +": Bad magician!\n")
    else:
        fout.write("Case #" + str(case+1) +": Volunteer cheated!\n")
