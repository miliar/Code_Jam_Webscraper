with open("test.txt", "r") as file:
    with open("out.txt", "w") as outFile:
        t = int(file.readline())
        for i in range(1,t+1): #Main loop
            g1 = int(file.readline())
            l1 = ""
            for j in range(1,5):
                if (j == g1):
                    l1 = file.readline()
                else:
                    file.readline()
            
            l1 = l1.rstrip().split(" ")
            g2 = int(file.readline())
            l2 = ""
            for j in range(1,5):
                if (j == g2):
                    l2 = file.readline()
                else:
                    file.readline()
            l2 = l2.rstrip().split(" ")
            answer = 0
            answerCount = 0
            for l in l1:
                if (l in l2):
                    answer = int(l)
                    answerCount = answerCount +1

            if (answerCount == 0):
                outFile.write("Case #" + str(i) + ": Volunteer cheated!\n")
            elif (answerCount == 1):
                outFile.write("Case #" + str(i) + ": "+ str(answer) + "\n")
            else:
                outFile.write("Case #" + str(i) + ": Bad magician!\n")
            
                
    
