infile = open('b_in.txt', 'r')
outfile = open('b_out.txt', 'w')
num_cases = int(infile.readline().strip())

for i in xrange(num_cases):
    C, F, X = [float(j) for j in infile.readline().strip().split()]
    # print C, F, X
    secs = 0.0
    old_secs = float('inf')
    cps = 2.0
    farms_bought = 0

    while True:
        for j in range(farms_bought):
            secs += C / cps
            cps += F

        secs += X / cps

        if secs > old_secs:
            secs = old_secs
            break

        old_secs = secs
        secs = 0.0
        cps = 2.0
        farms_bought += 1

    outfile.write('Case #' + str(i+1) + ': ' + str(secs) + '\n')

infile.close()
outfile.close()
