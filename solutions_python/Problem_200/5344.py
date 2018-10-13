myFile = open('/Users/sinapilehchiha/Desktop/B-small-attempt2.in.txt')
lines = myFile.readlines()
myList = [int(number) for number in lines]
del myList[0]
myStrList = list(map(str, myList))
for i in range(100):
    myStrList[i] = [int(d) for d in myStrList[i]]
#print (myStrList)
myIntList = myStrList

for i in range(100):
    iterNum = int(''.join([str(x) for x in myIntList[i]]))
    if iterNum == 10:
        print ("Case #{}: {}".format(i + 1, 9))
    if iterNum < 10:
        print ("Case #{}: {}".format(i + 1, iterNum))
    else:
        while iterNum != 0:
            if len(myIntList[i]) == 3:
                if myIntList[i][0] <= myIntList[i][1]:
                    if myIntList[i][1] <= myIntList[i][2]:
                        print ("Case #{}: {}".format(i + 1, iterNum))
                        break;
                    else:
                        previous_element = int(''.join([str(x) for x in myIntList[i]])) - 1
                        iterNum = iterNum - 1
                        myIntList[i] = [int(d) for d in list(str(iterNum))]
                else:
                    previous_element = int(''.join([str(x) for x in myIntList[i]])) - 1
                    iterNum = iterNum - 1
                    myIntList[i] = [int(d) for d in list(str(iterNum))]
            
            
            
            
            else:
                if myIntList[i][0] <= myIntList[i][1]:
                    print ("Case #{}: {}".format(i + 1, iterNum))
                    break;
                else:
                    previous_element = int(''.join([str(x) for x in myIntList[i]])) - 1
                    iterNum = iterNum - 1
                    myIntList[i] = [int(d) for d in list(str(iterNum))]