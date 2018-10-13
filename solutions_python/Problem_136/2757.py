import re

def string_to_list_of_floats(string):
    list_of_strings = re.split("\s", string)
    list_of_ints = map(float, list_of_strings)
    return list_of_ints

input = open("input.txt", 'r')

num_of_test_cases = int(input.readline()[:-1])
total_time = 0

for i in range(1,num_of_test_cases + 1):
    total_time = 0
    rate_of_production = 2
    parameters = string_to_list_of_floats(input.readline()[:-1])
    C = parameters[0]
    F = parameters[1]
    X = parameters[2]

    time_to_win = float(X/rate_of_production)
    time_to_win_with_new_factory = float(C/rate_of_production) + float(X/(rate_of_production+F))

    if X < C:
        print "Case #" + str(i) + ": " + str(float(X/2))
    else:
        while(time_to_win_with_new_factory < time_to_win):
            total_time = total_time + float(C/rate_of_production)
            rate_of_production = rate_of_production + float(F)
            time_to_win = float(X/rate_of_production)
            time_to_win_with_new_factory = float(C/rate_of_production) + float(X/(rate_of_production+F))

        total_time = total_time + float(X/rate_of_production)
        print "Case #" + str(i) + ": " + str(total_time)
        
