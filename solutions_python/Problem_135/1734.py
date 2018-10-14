__author__ = 'waigx'

fileHandle = open('file.in', 'r')
outputHandle = open('file.out.txt', 'w')


def check_repeat(array_a, array_b):
    result = 0
    the_number = -1
    for i in range(len(array_a)):
        for j in range(len(array_b)):
            if array_a[i] == array_b[j]:
                result += 1
                the_number = array_a[i]
    return [result, the_number]


caseNumber = int(fileHandle.readline())

for i in range(caseNumber):
    lineNumber = int(fileHandle.readline()) - 1
    for temp_i in range(4):
        temp_array = fileHandle.readline()
        if temp_i == lineNumber:
            array_a = [int(j) for j in temp_array.split(" ")]

    lineNumber = int(fileHandle.readline()) - 1
    for temp_i in range(4):
        temp_array = fileHandle.readline()
        if temp_i == lineNumber:
            array_b = [int(j) for j in temp_array.split(" ")]

    [repeat_time, the_number] = check_repeat(array_a, array_b)

    outputHandle.write("Case #" + str(i + 1) + ": ")

    if repeat_time < 1:
        outputHandle.write("Volunteer cheated!\n")
    if repeat_time == 1:
        outputHandle.write(str(the_number)+"\n")
    if repeat_time > 1:
        outputHandle.write("Bad magician!\n")

fileHandle.close()
outputHandle.close()