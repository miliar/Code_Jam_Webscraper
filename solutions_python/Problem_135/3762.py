f = open("A-small-attempt0.in")

def check(ar1,ar2):
    hit = 0
    for i in range(len(ar1)):
        for j in range(len(ar2)):
            if (ar1[i] == ar2[j]):
                hit += 1
                val = ar1[i]
                if (hit>1):
                    return "Bad magician!"

    if(hit==1):
        return val
    if(hit==0):
        return "Volunteer cheated!"



for i in range(1):

    data1 = f.readline()

    #print data1
    numOfTestCase = int(data1)

for i in range(numOfTestCase):
    data1 = f.readline()
    row1 = int(data1)
    for j in range(4):
        table = f.readline()
        if ( j+1 == row1):
            table1 = table
            #print table1.split()

    data1 = f.readline()
    row2 = int(data1)
    for j in range(4):
        table = f.readline()
        if ( j+1 == row2):
            table2 = table
            #print table2.split()

    checkVal = check(table1.split(), table2.split())

    print "Case #"+str(i+1)+": "+str(checkVal)

f.close()
