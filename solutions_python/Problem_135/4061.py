def readNumbers (f):
    return [int(x) for x in f.readline().split(' ')]

def guess(fileName):
    f = open(fileName)
    n = int(f.readline())
    for i in range(0,n):
        g1 = int(f.readline())
        l1 = [readNumbers(f), readNumbers(f), readNumbers(f), readNumbers(f)]
        g2 = int(f.readline())
        l2 = [readNumbers(f), readNumbers(f), readNumbers(f), readNumbers(f)]
        r = [val for val in l1[g1-1] if val in l2[g2-1]]
        if (len(r) == 1):
            print ("Case #{0}: {1}".format(i+1,r[0]))
        else:
            if (len(r) == 0):
                print ("Case #{0}: {1}".format(i+1,"Volunteer cheated!"))
            else:
                print ("Case #{0}: {1}".format(i+1,"Bad magician!"))
    f.close()
    
    
