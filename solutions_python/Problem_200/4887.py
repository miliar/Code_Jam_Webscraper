# Code by Connor Thompson for CodeJam 2017

file = open('B-small-attempt0.in.txt')
numberOfCases = int(file.readline())  # Get first line to get number of test cases T
caseCounter = 1  # Keep track of what case we're on for output
running = True
for j in range(0, numberOfCases):
    singleDigit = False
    currentNumber = file.readline()  # Get current number

    # If end of file, break
    if currentNumber == '\n' or currentNumber == '':
        running = False
        break

    # If single digit number, print it
    if len(currentNumber) == 2:
        print('Case #' + str(caseCounter) + ': ' + str(currentNumber), end="")
        singleDigit = True

    currentNumber = int(currentNumber)  # Convert to int after string comparison

    tidyNumber = currentNumber
    finalTidyNumber = 0  # Keeps track of final tidy number counter

    while tidyNumber > 0 and not singleDigit:
        tidyNumberList = list(str(tidyNumber))  # Get as list so we can compare adjacent numbers
        tidyNumberBool = False
        for i in range(0, len(tidyNumberList) - 1):
            if tidyNumberList[i] <= tidyNumberList[i + 1] and i + 1 <= len(tidyNumberList) - 1:
                tidyNumberBool = True
                if i == len(tidyNumberList) - 2:
                    finalTidyNumber = tidyNumber
                    print('Case #' + str(caseCounter) + ': ' + str(finalTidyNumber))
                    tidyNumber = 0

            if tidyNumberList[i] > tidyNumberList[i + 1] and i + 1 <= len(tidyNumberList) - 1:
                tidyNumber -= 1
                break

    caseCounter += 1
