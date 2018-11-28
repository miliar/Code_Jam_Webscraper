with open("input.txt","r") as read:
    with open("output.txt", "w") as write:
        total = int(read.readline())

        for l in xrange(total):
            guess = int(read.readline())
            for i in xrange(4):
                if (i == guess -1):
                    line = read.readline()
                else:
                    read.readline()
            a = [int(i) for i in str.split(line)]
            
            pick = int(read.readline())
            for i in xrange(4):
                if (i == pick-1):
                    line = read.readline()
                else:
                    read.readline()
            b = [int(i) for i in str.split(line)]
            r = 0
            c = 0
            for i in a:
                for j in b:
                    if i == j:
                        r+=1
                        c = i
            if (r >1 ):
                write.write("Case #" + str(l+1) + ": Bad magician!\n")
            elif (r==0):
                write.write("Case #" + str(l+1) + ": Volunteer cheated!\n")
            else:
                write.write("Case #" + str(l+1) + ": "+str(c) + "\n")
                
    write.close()
read.close()
