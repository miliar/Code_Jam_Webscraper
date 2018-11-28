infile = open("A-large.in", "r")
outfile = open("Aout.txt", "w")

total=0
t = int(infile.readline().rstrip())
for z in range(1, t+1):
    raw = infile.readline().split()
    n, disc = int(raw[0]), int(raw[1])
    file = infile.readline().split()
    file = [int(i) for i in file]
    file = sorted(file)
    solution=0
    while len(file)>0:
        #print(file)
        if len(file)==1:
            solution+=1
            break
        lookat = file[0]
        distance = 1000000000
        mincurr=-1
        for i in range(1, len(file)):
            if lookat+file[i]<=disc:
                if disc-lookat-file[i]<distance:
                    distance = disc-lookat-file[i]
                    mincurr = i
        solution+=1
        if mincurr!=-1:
            del file[mincurr]
            del file[0]
        else:
            del file[0]
    output = "Case #"+str(z)+": "+str(solution)+"\n"
    print(output)
    outfile.write(output)

infile.close()
outfile.close()
