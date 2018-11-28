# Google Code Jam 2014 Qualifying question B

infile = open('B-large.in', 'r')
outfile = open('B_large.txt', 'w')

n = infile.readline()

for case in range(1, int(n) + 1):
    total = 0.0
    rate = 2.0
    line = infile.readline()
    line = line.split(' ')
    cost, addrate, target = float(line[0]), float(line[1]), float(line[2][:-1])
    while True:
        currtime = target / rate
        newtime = (cost / rate) + (target / (rate + addrate))
        if currtime < newtime:
            total += currtime
            output = 'Case #{0}: {1}'.format(str(case), str("%.7f" % total))
            outfile.write(output + '\n')
            break
        else:
            total += cost / rate
            rate += addrate

infile.close()
outfile.close()
