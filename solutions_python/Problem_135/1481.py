f = open('/home/cse/btech/cs1130260/workfile.txt')
sumit = open("/home/cse/btech/cs1130260/output.txt","w")
a = int(f.readline())
x = 1
while (a > 0):
    firstanswer = int(f.readline())
    firstrow1 = f.readline()
    firstrow2 = f.readline()
    firstrow3 = f.readline()
    firstrow4 = f.readline()
    secondanswer = int(f.readline())
    secondrow1 = f.readline()
    secondrow2 = f.readline()
    secondrow3 = f.readline()
    secondrow4 = f.readline()
    if (firstanswer == 1):
        b = firstrow1.split()
    elif (firstanswer == 2):
        b = firstrow2.split()
    elif (firstanswer == 3):
        b = firstrow3.split()
    elif (firstanswer == 4):
        b = firstrow4.split()
    if (secondanswer == 1):
        c = secondrow1.split()
    elif (secondanswer == 2):
        c = secondrow2.split()
    elif (secondanswer == 3):
        c = secondrow3.split()
    elif (secondanswer == 4):
        c = secondrow4.split()
    i = 0
    k = 0
    while (i <= 3) and (k < 2):
        j = 0
        while (j <=3) and (k < 2):
            if (b[i] == c[j]):
                l = j
                k = k+1
                j = j+1
            else:
                j = j+1
        i = i+1
    if (k == 1):
        sumit.write("Case #%s: %s\n" % (x,int(c[l])))
    if (k == 2):
        sumit.write("Case #%s: Bad Magician!\n" % (x))
    if (k == 0):
        sumit.write("Case #%s: Volunteer cheated!\n" % (x))
    x = x+1
    a = a-1
sumit.close()
            
            

