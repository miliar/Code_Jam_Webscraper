import sys

fin = open("wire_try.in","r")
fout = open("wire.out","w")

t = int(fin.readline().strip())

for i in range(t):
    intersect = 0
    wires=[]
    nwire = int(fin.readline().strip())
    for j in range(nwire):
        temp = fin.readline().strip().split();
        wires.append(temp)
    #print wires
    #for k in range(len(wires)):
    k = 0
    while True:
        for l in range(len(wires)):
            if (int(wires[k][0]) > int(wires[l][0])):
                #print "inside greater if"
                if (int(wires[k][1]) < int(wires[l][1])):
                    #print "inside greater nested if"
                    intersect += 1
            elif (int(wires[k][0]) < int(wires[l][0])):
                #print "inside lesser if"
##                print wires[k][1]
##                print wires[l][1]
                if (int(wires[k][1]) > int(wires[l][1])):
                    #print "inside lesser if nested"
                    intersect += 1
        wires.pop(k)
        k += 1
        if k >= len(wires):
            break
        #print x
        #print wires

        

    if (i != t-1):
        output =  "Case #"+ str(i+1) + ": " +str(intersect) +"\n"
    else:
        output =  "Case #"+ str(i+1) + ": " +str(intersect)
    fout.write(output)
fin.close()
fout.close()
                    
                    
        
