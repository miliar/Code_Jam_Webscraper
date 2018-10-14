def cruise(filename, outname):
    infile = open(filename, "r+")
    outfile = open(outname, "w+")
    lines = infile.readlines()
    T = int(lines[0])
    line_num = 1
    for i in range(T):
        D = int(lines[line_num].split(" ")[0])
        N = int(lines[line_num].split(" ")[1])
        max_time = 0
        line_num += 1
        for j in range(N):
            K_i = int(lines[line_num+j].split(" ")[0])
            S_i = int(lines[line_num+j].split(" ")[1])
            max_time = max(max_time, float(D-K_i)/S_i)
        line_num += N
        max_speed = float(D)/max_time
        outfile.write("Case #" + str(i+1) + ": " + str(max_speed) + "\n")
    infile.close()
    outfile.close()
