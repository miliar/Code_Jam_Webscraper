f = open("input.txt", "r")
fout = open("output.txt", "w")
normal = "abcdefghijklmnopqrstuvwxyz"
cripted ="yhesocvxduiglbkrztnwjpfmaq"
i = 0
tot = f.readlines()
L = tot[0]
while(i<(int(L))):
    i+=1
    fout.write("Case #" + str(i) + " ")
    for x in range(len(tot[i])):
        print tot[i][x]
        if(tot[i][x] == "\n"):
            continue
        if(tot[i][x] == " "):
            fout.write(" ")
        else:
            fout.write(cripted[normal.index(tot[i][x])])
    fout.write("\n")
fout.close()
f.close()
