from math import sqrt, floor

totalFiltered = []
num = 1
B = pow(10,7)
while num <= B:
    snum = str(num)
    if snum == snum[::-1]:
        strsquared = str(num * num)
        if strsquared == strsquared[::-1]:
            totalFiltered.append(num * num)
    num += 1                    

f = open("C-large-1.in","r")
output = open("outputF.txt", "w")
lineas = f.readlines()
lineas = lineas[1:]

for index,linea in enumerate(lineas):
    numsLinea = linea.split()
    A = int(numsLinea[0])
    B = int(numsLinea[1])
    accepted = [ x for x in totalFiltered if x >= A and x<=B ]
    output.write("Case #" + str(index + 1) + ": " + str(len(accepted)) + "\n")

output.write("\n")
output.close()
f.close()

