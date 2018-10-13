input_file = open("A-small-attempt0.in", "r")
output_file = open("A-small-attempt0.out", "w")

test_cases = int(input_file.readline())

caseNumber = 1

for length in range(test_cases):
    answerOne = int(input_file.readline())

    number = []

    gridOne = []
    gridTwo = []

    for val in range(4):
        rowOne = input_file.readline().split()
        gridOne.append(rowOne)

    answerTwo = int(input_file.readline())

    for val in range(4):
        rowTwo = input_file.readline().split()
        gridTwo.append(rowTwo)

    #Subtract 1 because iteration starts at 0
    hitListOne = gridOne[answerOne - 1]
    hitListTwo = gridTwo[answerTwo - 1]

    for char in range(len(hitListOne)):
        for val in range(len(hitListTwo)):
            if hitListOne[char] == hitListTwo[val]:
                number.append(hitListOne[char])

    if len(number) == 1:
        output_file.write("Case #" + str(caseNumber) + ": " + number[0] +"\n")
        caseNumber += 1
    elif len(number) > 1:
        output_file.write("Case #" + str(caseNumber) + ": Bad magician!" +"\n")
        caseNumber += 1
    elif len(number) == 0:
        output_file.write("Case #" + str(caseNumber) + ": Volunteer cheated!" +"\n")
        caseNumber += 1
    
input_file.close()
output_file.close()
