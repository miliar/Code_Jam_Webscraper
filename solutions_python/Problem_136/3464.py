with open("B-small-attempt1.in","r") as file:
    with open("output.out","w") as out:
        m = int(file.readline())
        for j in range(m):
            n = 1
            line = str(file.readline())
            c = float(line.split()[0])
            F = float(line.split()[1])
            x = float(line.split()[2])
            timeold = x/2
            while True:
                #rint(timeold)
                time = x/(2+n*F)
                for i in range(n):
                    time = time+c/(2+i*F)
                if time > timeold:
                    break
                else:
                    timeold = time
                    n+=1
            out.write("Case #{}: {}\n".format(j+1,timeold))