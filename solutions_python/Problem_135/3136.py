
filename = "A-small-attempt3.in"
out_filename = filename.split(".")[0] + ".out"


out_f = file(out_filename, "w")
f = file(filename, "r")
cases = int(f.readline())

for i in range(0,cases):
        ans1 = int(f.readline())
        row11 = f.readline().replace("\n", "").split(" ")
        row12 = f.readline().replace("\n", "").split(" ")
        row13 = f.readline().replace("\n", "").split(" ")
        row14 = f.readline().replace("\n", "").split(" ")
        rows1 = [row11,row12,row13,row14]
        
        ans2 = int(f.readline())
        row21 = f.readline().replace("\n", "").split(" ")
        row22 = f.readline().replace("\n", "").split(" ")
        row23 = f.readline().replace("\n", "").split(" ")
        row24 = f.readline().replace("\n", "").split(" ")
        rows2 = [row21,row22,row23,row24]
        
        ans = None
        matches = 0
        for item in rows2[(ans2-1)]:
                if item in rows1[ans1-1]:
                        matches += 1
                        ans = item

        out_f.write( "Case #" + str(i+1) + ": ")
        
        if matches == 0:
                out_f.write( "Volunteer cheated!\n")
        elif matches == 1:
                out_f.write(str(int(ans)) + "\n")
        else:
                out_f.write("Bad magician!\n")


out_f.close()

