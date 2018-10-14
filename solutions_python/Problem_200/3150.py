def find_tidy(filename):
    infile = open(filename, "r+")
    outfile = open("tidy_out.txt", "w+")
    inlines = infile.readlines()
    for i in range(1, len(inlines)):
        N = str(int(inlines[i]))
        N_l = [N[j] for j in range(len(N))]
        for j in range(len(N_l)-2, -1, -1):
            if int(N_l[j]) > int(N_l[j+1]):
                N_l[j] = str(int(N_l[j])-1)
                for k in range(j+1, len(N)):
                    N_l[k] = "9"
                """if j+1 == len(N)-1:
                    N_l[j+1] = "9"
                else:
                    N_l[j+1] = N_l[j+2]"""
        if N_l[0] == '0':
            N_l = ['9']*(len(N)-1)
        outfile.write("Case #" + str(i) + ": " + str(int(''.join(N_l))) + "\n")
    infile.close()
    outfile.close()
