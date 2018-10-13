infile = open("Dsmall.txt", "r")
outfile = open("Dsmallout.txt", "w")

tcase = int(infile.readline().rstrip())
for z in range(1, tcase+1):
    data = infile.readline().rstrip()
    x, r, c = data.split()
    x = int(x)
    r = int(r)
    c = int(c)
    solution=""
    if x==1:
        solution = "GABRIEL"
    elif x==2:
        if r*c%2==0:
            solution = "GABRIEL"
        else:
            solution = "RICHARD"
    elif x==3:
        if r*c%3!=0:
            solution = "RICHARD"
        else:
            if r*c==3:
                solution = "RICHARD"
            else:
                solution = "GABRIEL"
    else:
        if r*c%4!=0:
            solution = "RICHARD"
        else:
            if r*c==4 or r*c==8:
                solution = "RICHARD"
            else:
                solution = "GABRIEL"
    outline = "Case #"+str(z)+": "+solution+"\n"
    outfile.write(outline)


infile.close()
outfile.close()
