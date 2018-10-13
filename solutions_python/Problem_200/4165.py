# Open file
file = open('example.in').read()
lines = file.splitlines()

amount = lines[0]
values = lines[1:]

outputs = []

for value in values:
    valList = list(value)

    # Look for first digit that causes this number to be untidy (from left)
    last = 0
    change = False

    for index in range(len(value)):

        digit = value[index]
        if int(digit) >= last:
            last = int(digit)
            continue

        else:
            change = True
            break

    # Change value
    if change:

        # What is the index of the closest lower digit to the left
        start = valList[index - 1]
        done = False
        for dIndex in range(index):
            vIndex = index - dIndex - 1

            if valList[vIndex] < start:
                changeIndex = vIndex + 1
                done = True

        if not done: # All digits before incorrect one are the same
            changeIndex = 0

        # Change digits to ints
        for i in range(len(valList)): valList[i] = int(valList[i])

        # Change wrong digit
        valList[changeIndex] -= 1

        # Change following digits
        for valIndex in range(len(valList) - changeIndex - 1):
            valIndex += changeIndex + 1

            valList[valIndex] = 9

    outputs.append(valList)


# Fix outputs
newOuts = []
for index in range(len(outputs)):
    out = outputs[index]
    numberStr = ''

    for value in out:
        numberStr += str(value)

    val = 'Case #' + str(index + 1) + ': ' + str(int(numberStr))
    newOuts.append(val)

output = '\n'.join(newOuts)

writeFile = open('example.out', 'w')
writeFile.write(output)
writeFile.close()