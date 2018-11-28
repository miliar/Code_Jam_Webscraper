infile = open("Alarge.txt", "r")
outfile = open("Alargeout.txt", "w")

tcase = int(infile.readline().rstrip())
for z in range(1, tcase+1):
    data = infile.readline().rstrip()
    smax, shyness = data.split()
    smax = int(smax)
    shyness = str(shyness)
    standing = 0
    needed=0
    for i in range(0, smax+1):
        current = int(shyness[i])
        #print(i, standing, current, needed)
        if standing>=i:
            standing+=current
        else:
            needed+=(i-standing)
            standing=current+i
        #print(i, standing, current, needed, "2")
    outline = "Case #"+str(z)+": "+str(needed)+"\n"
    outfile.write(outline)

infile.close()
outfile.close()
