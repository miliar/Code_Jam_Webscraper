
#inputFile = open('test.txt', 'r')
#inputFile = open('A-small-attempt0.in', 'r')
inputFile = open('A-large.in', 'r')


# keep track of number of cases
num_case = int(inputFile.readline())

for case in range(1, num_case+1):

    # get input
    num_steps = int(inputFile.readline())
    mushrooms_string = inputFile.readline()
    mushrooms_string_array = mushrooms_string.split()
    mushrooms = [int(i) for i in mushrooms_string_array]

    # calculate using method 1
    plate = mushrooms[0]
    eaten = 0
    for i in range(1, len(mushrooms)):
        diff = plate - mushrooms[i]
        if diff >= 0:
            eaten += diff
        plate = mushrooms[i]
    y = eaten

    # calculate using method 2
    diff = [mushrooms[i] - mushrooms[i+1] for i in range(len(mushrooms)-1)]
    eat_rate = max(diff)
    plate = mushrooms[0]
    eaten = 0
    for i in range(1, len(mushrooms)):
        if plate >= eat_rate:
            eaten += eat_rate
        else:
            eaten += plate
        plate = mushrooms[i]
    z = eaten

    print 'Case #' + str(case) + ':', y, z
