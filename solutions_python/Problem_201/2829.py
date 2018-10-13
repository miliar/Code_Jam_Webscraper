import math;
name = "C-small-2-attempt3"
file = open(name + ".in", "r")

cases = int(file.readline())
#cases = 7

finishedListY = []
finishedListZ = []


def bigNum(data, last):
    #"this returns index of the first biggest number in a list"
    if(last != -1 and last <= len(data) - 1):
        i = last
    else:
        i = len(data) - 1
    while(data[i] == 0):
        #print(i)
        i -= 1
    return i



i = 0
while(i < cases):
    #get our number
    i += 1
    temp = file.readline()
    temp2 = temp.split(" ")
    n = int(temp2[0])
    k = int(temp2[1])

    spaces = [0] * n
    spaces[n-1] = 1
    print("--------------")
    print(str(i) + " - " + str(n) + " - " + str(k))

    if(n == k):
        finishedListY.append(0)
        finishedListZ.append(0)
        print("n = k")
        continue
    """if((n-1) == k):
        finishedListY.append(0)
        finishedListZ.append(0)
        print("n-1 = k")
        continue"""
    bNum = -1
    #find a place for each person
    while(k > 0):
        #get the leftmost of the biggest spaces
        bNum = bigNum(data = spaces, last = bNum)
        #bNum = int(math.ceil(bNum))
        #print("bNum: " + str(bNum) + " - " + str(spaces[bNum]) + " * " + str(spaces))
        
        half = (bNum+1) / 2
        
        spaces[bNum] = spaces[bNum] - 1
        """if(spaces[bNum] == 0):
            indent = 0
            temp = []
            for num in spaces:
                if(indent <= bNum):
                    temp.append(num)
                indent += 1
            spaces = temp    
        """            
        if(int(half) == math.ceil(half)):      # 6 > 3
            half = int(half)
            spaces[half-1]    += 1    # 3
            spaces[half-2]  += 1    # 2,3
            myY = half
            myZ = half-1
            #print("ow yis")
        else: #7 > 3.5
            half = int(math.ceil(half)) # 4
            spaces[half-2]  += 1    # 3
            spaces[half-2]  += 1    # 3,3
            myY = half-1
            myZ = half-1
            #print("nope")
            
        #print(str(half) + " - " + str(isinstance(half, int)))
        #print(str(k) + " - " + str(myY) + " - " + str(myZ) + " * " + str(spaces))
        
        k-=1
        #if(int(k/10000) == math.ceil(k/10000)):
        #    print(str(k))
        if(k == 0):
            finishedListY.append(myY)
            finishedListZ.append(myZ)
    

#write the answer file

outputFile = open(name + ".out", "w")

m = 1

while (m <= cases):

    outputFile.write("Case #" + str(m) + ": " +          #x
                     str(finishedListY[m-1]) + " " +     #y
                     str(finishedListZ[m-1]) + "\n")     #z
    m += 1

outputFile.close()

print("DONE")

