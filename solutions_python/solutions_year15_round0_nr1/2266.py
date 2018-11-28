# GCJ 2015 Q1

infile = open("A-large.in", "r")
outfile = open("A-Large.txt", "w")

cases = infile.readline()
for case in range(int(cases)):
    line = infile.readline()
    line = (line.split(' '))[1]
    line = line[:-1]
    add_members = 0
    curr_sum = 0
    for i in range(len(line)):
        if curr_sum + add_members < i:
            add_members += (i - (curr_sum + add_members))
        curr_sum += int(line[i])
    print(case)
    print(add_members)
    if case < int(cases):
        outfile.write("Case #{0}: {1} \n".format(str(int(case) + 1), add_members))
    else:
        outfile.write("Case #{0}: {1}".format(str(int(case) + 1), add_members))

infile.close()
outfile.close()
