infile = open('a_in.txt', 'r')
outfile = open('a_out.txt', 'w')
num_cases = int(infile.readline().strip())

for i in xrange(num_cases):
    ans1 = int(infile.readline().strip())
    line1 = None
    line2 = None
    overlap = []
    for j in xrange(4):
        tmp = infile.readline().strip()
        if j == ans1 - 1:
            line1 = [int(k) for k in tmp.split()]
    ans2 = int(infile.readline().strip())
    for j in xrange(4):
        tmp = infile.readline().strip()
        if j == ans2 - 1:
            line2 = [int(k) for k in tmp.split()]
    for j in line1:
        if j in line2:
            overlap.append(j)
    if len(overlap) == 1:
        outfile.write('Case #' + str(i+1) + ': ' + str(overlap[0]) + '\n') 
    elif len(overlap) < 1:
        outfile.write('Case #' + str(i+1) + ': Volunteer cheated!' + '\n') 
    else:
        outfile.write('Case #' + str(i+1) + ': Bad magician!' + '\n') 

infile.close()
outfile.close()
