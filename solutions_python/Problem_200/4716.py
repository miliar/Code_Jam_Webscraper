file = open("B-small-attempt4.in", "r")
ofile = open("output.txt", "w")
intCase = int(file.readline()[:-1])
for i in range(intCase):
    strLimit = file.readline()[:-1]
    intLimit = [int(i) for i in strLimit]
    for j in range(len(intLimit)):
        intLimit[j] = int(intLimit[j])
    good = True
    samezies = False
    counter = 0
    while counter < len(intLimit)-1 and good == True:
        if intLimit[counter] == int(intLimit[counter+1]):
            samezies = True
        if intLimit[counter] > int(intLimit[counter+1]):
            good = False
            counter -= 1
            if samezies == True:
                counter -= 1
        counter += 1
    output = ""
    if good == False:
        for j in range(len(intLimit)):
            if j < counter:
                output += str(intLimit[j])
            elif j == counter:
                if j != 0 or intLimit[j] != 1:
                    output += str(intLimit[j]-1)
            else:
                output += "9"
    else:
        output = strLimit
    if i != intCase-1:
        ofile.write("Case #" + str(i+1) + ": " + output + "\n")
    else:
        ofile.write("Case #" + str(i+1) + ": " + output)
ofile.close()
    
    
