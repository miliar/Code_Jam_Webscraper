__author__ = 'Dan'

# numberOfTests = input()
# inputFile = open('A-small-attempt0.in', 'r')
inputFile = open('A-large.in', 'r')
# inputFile = open('input.txt', 'r')
outputFile = open('output.txt', 'w')
numberOfTests = inputFile.readline()

for testNumber in range(int(numberOfTests)):
    nextLine = inputFile.readline().split()
    maxShyness = int(nextLine[0])
    shynessPeople = str(nextLine[1])
    numberOfPeopleAvailable = 0
    answer = 0
    index = 0
    gen = (person for person in shynessPeople if index <= maxShyness)
    for person in gen:
        if index > 0 and index > numberOfPeopleAvailable and int(person) > 0:
            answer += index - numberOfPeopleAvailable
            numberOfPeopleAvailable += index - numberOfPeopleAvailable
        numberOfPeopleAvailable += int(person)
        index += 1

    outputFile.write('Case #' + str(testNumber + 1) + ': ' + str(answer) + '\n')