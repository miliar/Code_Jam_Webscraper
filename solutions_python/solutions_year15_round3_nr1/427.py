import math

fhr = open("input.txt",'r')
fhw = open("output.txt",'w')

f = fhr.readlines()
fhr.close()
Cases = int(f[0].strip())

for i in range(0,Cases):
    C = int(((f[i+1].strip()).split())[1])
    W = int(((f[i+1].strip()).split())[2])
    Score = math.ceil((C/W)) + W - 1
    fhw.write("Case #" + str(i+1) + ": " + str(Score) + "\n")
fhw.close()
