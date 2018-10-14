

with open("input.txt","r") as read:
    with open("output.txt", "w") as write:
        test = int(read.readline())

        for l in range(test):
            fstpick = int(read.readline())
            st = ''
            for i in range(4):
                if i == fstpick -1:
                    line = read.readline()
                    
                    st = line.split()
                else:
                    read.readline()
            
  
            
            pick = int(read.readline())
            st2 = ''
            for i in range(4):
                if i == pick-1:
                    line = read.readline()
                    st2 = line.split()
                else:
                    blah = read.readline()

            
 
            r = 0
            c = 0
    

            
            for i in st:
                for j in st2:
                    if i == j:
                        r+=1
                        c = i
            if r >1 :
                write.write("Case #" + str(l+1) + ": Bad magician!\n")
            elif r==0:
                write.write("Case #" + str(l+1) + ": Volunteer cheated!\n")
            else:
                write.write("Case #" + str(l+1) + ": "+str(c) + "\n")
                
    write.close()
read.close()
