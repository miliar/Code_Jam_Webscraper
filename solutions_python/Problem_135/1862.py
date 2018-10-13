with open("A-output.txt", "w") as output:
    with open("A-small-attempt0.in", "r") as input:
        N = int(input.readline().strip())
        for i in range (0,N):
            ans1 = int(input.readline().strip())
            arr1 = list()
            arr2 = list()
            for j in range(0,4):
                arr1.append(input.readline().strip().split())
            row1 = arr1[ans1 - 1]
            ans2 = int(input.readline().strip())
            for j in range(0,4):
                arr2.append(input.readline().strip().split())
            row2 = arr2[ans2 - 1]
            common = list(set(row1).intersection(set(row2)))
            #print (common)
            #print ('Case #' + str(i+1) + ": ")
        
            if (len(common)) == 1: print (('Case #' + str(i+1) + ": " + common[0]), file = output)
            elif (len(common)) > 1: print (('Case #' + str(i+1) + ": " + 'Bad magician!'), file = output)
            else: print (('Case #' + str(i+1) + ": " + 'Volunteer cheated!'), file = output)



