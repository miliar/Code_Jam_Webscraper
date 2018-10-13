infile = open("C-small-attempt4.in", "r")
lines = infile.readlines()

count = 0
a = 0
b = 0
c = ""


check1 = ["1", "i", "j", "k", "i", "-1", "k", "-j", "j", "-k", "-1", "i", "k", "j", "-i", "-1"]
check2 = ["11", "1i", "1j", "1k", "i1", "ii", "ij", "ik", "j1", "ji", "jj", "jk", "k1", "ki", "kj", "kk"]

for line in lines:
    if count == 0:
        pass
    else:
        solved = False
        solved_i = False
        solved_j = False
        solved_k = False
        if count % 2 == 1:
            line = line[:-1].split()
            a = int(line[0])
            b = int(line[1])
        else:
            c = line[:-1]*b
            while solved == False and len(c) > 1:
                if c[0] == "i" and solved_i == False:
                    solved_i = True
                    c = c[1:]
                if c[0] == "j" and solved_i == True and solved_j == False:
                    solved_j = True
                    c = c[1:]
                if len(c) > 1:
                    for i in range(len(check1)):
                        if c[0] == "-":
                            if check2[i] == c[1:3]:
                                c = "-" + check1[i] + c[3:]
                                break
                        elif check2[i] == c[:2]:
                            c = check1[i] + c[2:]
                            break
                    if c[:2] == "--":
                        c = c[2:]
                    if len(c) == 2 and c[0] == "-":
                        break
            outfile = open("outfileC.txt", "a")
            if solved_j and solved_i and c == "k":
                outfile.write("Case #" + str((count)//2) + ": YES\n")
            else:
                outfile.write("Case #" + str((count)//2) + ": NO\n")
            outfile.close()
            
    count += 1

infile.close()
