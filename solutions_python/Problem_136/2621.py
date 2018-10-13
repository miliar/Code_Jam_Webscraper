import sys
fileName = sys.argv[1]
inputFile = open(fileName, 'r')
num_cases = int(inputFile.readline())

for test_case_num in range(1, num_cases + 1):
    time_taken = 0
    current_rate = 2.0

    variables = [float(x) for x in inputFile.readline().split(" ")]
    farm_cost = variables[0]
    farm_rate = variables[1]
    cookie_goal = variables[2]

    while True:
        if (cookie_goal / current_rate) <= ((farm_cost / current_rate) + (cookie_goal / (current_rate + farm_rate))):
            time_taken += (cookie_goal / current_rate)
            break
        else:
            time_taken += (farm_cost / current_rate)
            current_rate += farm_rate

    case_message = time_taken
    print ("Case #{0}: {1:.7f}".format(test_case_num, case_message))
