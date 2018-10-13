import sys

theFile = open(sys.argv[1], 'r')
testCases = int(theFile.readline())
#print("Number of Test Cases: ", testCases)

testCounter = 1
while(testCounter <= testCases):
    guess1 = int(theFile.readline())
    #print("Guess One: ", guess1)
    
    mat1 = []
    mat1.append(list(map(int,theFile.readline().split(' '))))
    mat1.append(list(map(int,theFile.readline().split(' '))))
    mat1.append(list(map(int,theFile.readline().split(' '))))
    mat1.append(list(map(int,theFile.readline().split(' '))))
    #print(mat1)
    
    
    guess2 = int(theFile.readline())
    #print("Guess Two: ", guess2)
    
    mat2 = []
    mat2.append(list(map(int,theFile.readline().split(' '))))
    mat2.append(list(map(int,theFile.readline().split(' '))))
    mat2.append(list(map(int,theFile.readline().split(' '))))
    mat2.append(list(map(int,theFile.readline().split(' '))))
    #print(mat2)
    
    set1 = set(mat1[guess1 - 1])
    #print(set1)
    set2 = set(mat2[guess2 - 1])
    #print(set2)
    
    intersectionSet = set1.intersection(set2)
    result = len(intersectionSet)
    #print(result)
    
    if result == 0:
        print("Case #{}: Volunteer cheated!".format(testCounter))
    elif result == 1:
        print("Case #{}: {}".format(testCounter, set1.intersection(set2).pop()))
    else:
        print("Case #{}: Bad magician!".format(testCounter))
            
    testCounter += 1
    #print()
    

theFile.close()
