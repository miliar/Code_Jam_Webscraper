f = open("A-small-attempt1.in","r")
g = open("A-small-attempt1.out","w")

cases = int(f.readline())

i = 0

while i < cases:

    params = f.readline().rstrip().split(" ")

    r = int(params[0])
    t = int(params[1])

    paintAvail = t
    
    ringCount = 0

    for j in range(1,1001,2):

        paintUsed = ((r+j)** 2) - ((r+(j-1))**2)

        paintAvail -= paintUsed

        if paintAvail < 0:
            break
        else:
            ringCount +=1
            

    i += 1
    print i
    g.write("Case #" + str(i) + ": " + str(ringCount) + "\n")

g.close()
        

        

    

    
