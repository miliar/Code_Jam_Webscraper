inputFile = open('input.in', 'r')
outputFile = open('output.txt', 'w')

testCases = int(inputFile.readline())
for n in range(1, testCases + 1):
    a1 = int(inputFile.readline())
    for i in range(1, 5):
        if i == a1:
            l1 = set(inputFile.readline().strip().split(" "))
        else:
            inputFile.readline()
    a2 = int(inputFile.readline())
    for i in range(1, 5):
        if i == a2:
            l2 = set(inputFile.readline().strip().split(" "))
        else:
            inputFile.readline()
    number = l1.intersection(l2)
    if len(number) == 0:
        answer = "Volunteer cheated!"
    elif len(number) > 1:
        answer = "Bad magician!"
    else:
        answer = str(number.pop())
    text = "Case #" + str(n) + ": " + answer + "\n"
    outputFile.write(text)
outputFile.close()
