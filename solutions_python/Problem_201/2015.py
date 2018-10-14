import os


def get_stall(stalls):
    if len(stalls) == 1:
        return stalls[0]
    else:
        stalls_with_max_distance = []
        for stall in stalls:
            if len(stalls_with_max_distance) == 0 or stalls_with_max_distance[0][2] == stall[2]:
                stalls_with_max_distance.append(stall)
            elif stalls_with_max_distance[0][2] < stall[2]:
                stalls_with_max_distance = []
                stalls_with_max_distance.append(stall)

        return stalls_with_max_distance[0]


def get_ls(stalls, possible_spot):
    number_of_empty_stalls = 0
    for i in xrange(possible_spot - 1, 0, -1):
        if stalls[i] == False:
            number_of_empty_stalls += 1
        else:
            return number_of_empty_stalls
    return number_of_empty_stalls


def get_rs(stalls, possible_spot):
    number_of_empty_stalls = 0
    for i in xrange(possible_spot + 1, len(stalls)):
        if stalls[i] == False:
            number_of_empty_stalls += 1
        else:
            return number_of_empty_stalls
    return number_of_empty_stalls


def seat_person(stalls):
    best_possible_stalls = []

    # Get Ls and Rs for every stall
    for i in xrange(0, len(stalls)):
        if stalls[i] == False:
            Ls = get_ls(stalls, i)
            Rs = get_rs(stalls, i)
            spot = (i, min(Ls, Rs), max(Ls, Rs))
            if len(best_possible_stalls) == 0 or best_possible_stalls[0][1] == spot[1]:
                best_possible_stalls.append(spot)
            elif best_possible_stalls[0][1] < spot[1]:
                best_possible_stalls = []
                best_possible_stalls.append(spot)

    stall = get_stall(best_possible_stalls)
    index = stall[0]
    stalls[index] = True
    return stalls, stall[1], stall[2]

with open('input.txt') as input_file:
    testCases = input_file.readlines()
numTestCases = testCases[0]
testCases.remove(numTestCases)
output_filename = 'output.txt'
if os.path.exists(output_filename):
    os.remove(output_filename)
min_max = []
for i in range(0, len(testCases)):
    x = testCases[i].split()
    number_stalls = x[0]
    number_people = x[1]
    stalls = [True] + int(number_stalls) * [False] + [True]
    for i in xrange(0, int(number_people)):
        stalls, minimum, maximum = seat_person(stalls)
    min_max.append((minimum, maximum))

with open(output_filename, 'a') as output_file:
    for i in xrange(0, len(min_max)):
        output_file.write('Case #' + str(i + 1) + ': ' +
                          str(min_max[i][1]) + ' ' + str(min_max[i][0]) + '\n')
