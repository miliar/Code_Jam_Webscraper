fin = open("input.txt", "r")
fout = open("output.txt", "w")
cases = eval(fin.readline())
for i in range(cases):
    line = fin.readline()
    fout.write("Case #" + (str)(i + 1))
    for word in reversed(line.split()):
         fout.write(" " + word)  
    fout.write("\n")
    
fin.close()
fout.close()
