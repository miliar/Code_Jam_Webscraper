f = open("D-small-attempt1.in","r")
#f = open("A-large.in","r")
g = open("test.txt","w")

cases = int(f.readline())
caseno = 1

for m in range(cases):
    g.write("Case #" + str(caseno) + ": ")

    line = f.readline().strip().split(" ")
    omino = int(line[0])
    row = int(line[1])
    col = int(line[2])

    possible = False

    if(row>=omino or col>=omino):
        if( row>= omino-1 and col >= omino-1):
            if((row*col)%omino==0):
                possible = True

    if(possible==True):
        g.write("GABRIEL" + "\n")
    else:
        g.write("RICHARD" + "\n")

    caseno = caseno+1

f.close()
g.close()



