fileIn = open("A-small-practice.in","r")
fileOut = open("Output.out","w")
fileIn.readline()




def istidy(x):
    x = str(x)
    s = False

    for i in range (1,len(x)):
        if len(x) == 1 :
            s = True
        elif int(x[i]) >= int (x[i-1]):
            s = True
        else :
            return False
    return True




def find(x):
    p = int(x)
    z = 0
    for i in range (1 ,int(p)+1) :
        if (istidy(i)):
            z = i
    return z

for y in range(1,101):

     x = fileIn.readline()
     z = find(x)


     fileOut.write("Case #" + str(y) + ": " + str(z) + "\n")

fileIn.close()
fileOut.close()


