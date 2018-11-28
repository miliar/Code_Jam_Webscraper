
# open input file
#inputFile = open('test.txt', 'r')
#inputFile = open('A-small-attempt2.in.txt', 'r')
inputFile = open('A-large.in.txt', 'r')


# keep track of number of cases
num_case = int(inputFile.readline())

for case in range(1, num_case+1):
    # get the next line
    next_line = inputFile.readline()
    value = next_line.split()

    # get the max number shyness level
    max_shyness = int(value[0])

    # get the number of audiences at each level
    shyness_numbers = [int(i) for i in value[1]]

    # initialize number of friends to invite
    num_friends = 0
    
    while (True):
        num_standing = 0
        for level in range(len(shyness_numbers)):
            if num_standing >= level:
                num_standing += shyness_numbers[level]

        # if not everyone is standing, get a friend with no shyness
        if num_standing < sum(shyness_numbers):
            shyness_numbers[0] += 1
            num_friends += 1
        else:
            break

    print 'Case #' + str(case) + ': ' + str(num_friends)

    
    
