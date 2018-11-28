

def checkarray(array1,array2):
    match = 0
    for i in array1:
        if (i in array2):
            match += 1
    return match

def readarray(file_to_read):
    array = list()
    for n in range(4):
        array.append(file_to_read.readline()[:-1].split(" "))
    return(array)

def returnmatch(array1,array2):
    for i in array1:
        for j in array2:
            if (i == j):
                return(i)

in_file = open("in", 'r')
out_file = open('out', 'w')


number_of_tests = int(in_file.readline()[:-1])

# For each test
for i in range(number_of_tests):
    row_1 = int(in_file.readline()[:-1]) - 1
    array1 = readarray(in_file)
    row_2 = int(in_file.readline()[:-1]) - 1
    array2 = readarray(in_file)

    match_number = checkarray(array1[row_1],array2[row_2])

    print(match_number)
    
    if (match_number == 0):
        out_file.write("Case #" + str(i+1) + ": Volunteer cheated!\n")

    if (match_number > 1):
        out_file.write("Case #" + str(i+1) + ": Bad magician!\n")

    if (match_number == 1):
        out_file.write("Case #" + str(i+1) + ": " + returnmatch(array1[row_1],array2[row_2])+"\n")

in_file.close()
out_file.close()
