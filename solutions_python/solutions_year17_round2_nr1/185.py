with open("A-large.in", "r") as ifile, open("out.txt", "w") as ofile:
    lines = ifile.readlines()
    T = int(lines[0])
    linesLeft = 0
    D = 0
    V = 0
    case = 0
    for i in range(1, len(lines)):
        if linesLeft == 0:
            if i>1:
                ofile.write("Case #{0}: {1:.6f}\n".format(case, V))
            case +=1
            sl = lines[i].split(" ")
            D = int(sl[0])
            linesLeft = int(sl[1])
            V = 0
        else:
            linesLeft-=1
            sl = lines[i].split(" ")
            d0 = int(sl[0])
            v0 = int(sl[1])
            #print(v0*D/(D-d0))
            if V == 0:
                V = v0*D/(D-d0)
            else:
                V = min(V, v0*D/(D-d0))
            
    ofile.write("Case #{0}: {1:.6f}\n".format(T, V))        
            
        