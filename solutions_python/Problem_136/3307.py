

file_in = open('b.in', 'r')
file_out = open('b.out', 'w')

n_case = int(file_in.readline())

R = 2.0
for i_case in range(n_case):
    C, F, X = (float(s) for s in file_in.readline().split())
    best = X/R
    i = 1
    running = C/R
    while running < best:
        best = min(best, running + X/(R + i*F))
        running += C/(R + i*F)
        i += 1
    file_out.write("Case #" + str(i_case+1) + ": " + str(best) + "\n")

file_in.close()
file_out.close()
