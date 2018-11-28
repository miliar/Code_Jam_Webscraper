def divide(number):
    dividedList = []
    if number % 2 == 1:
        dividedList += [number//2, -1, number//2]
    else:
        dividedList += [number//2 - 1, -1, number//2]
    return dividedList

def lastBathroomStall(numberStalls, numberPeople):
    stallList = [-1] + [numberStalls] + [-1]
    for i in range(numberPeople):
        maxNumber = max(stallList)
        maxIndex = stallList.index(maxNumber)
        divided = divide(maxNumber)
        stallList = stallList[:maxIndex] + divided + stallList[maxIndex + 1:]
    return divided

'''
numberTestCase = int(input())
testList = []
for i in range(numberTestCase):
    inputList = input().split()
    testList.append((int(inputList[0]), int(inputList[1])))
for j in range(numberTestCase):
    result = lastBathroomStall(testList[j][0], testList[j][1])
    print("Case #" + str(j+1) + ": " + str(result[2]) + " " + str(result[0]))
'''

file = open("C-small-1-attempt0.in")
output = open("Output File.txt","w")
numberTestCase = int(file.readline())
testList = []
for i in range(numberTestCase):
    inputList = file.readline().split()
    testList.append((int(inputList[0]), int(inputList[1])))
for j in range(numberTestCase):
    result = lastBathroomStall(testList[j][0], testList[j][1])
    output.write("Case #" + str(j+1) + ": " + str(result[2]) + " " + str(result[0]) + "\n")


file.close()
output.close()
