from __future__ import division


def solve(line):
    split_line = line.split(" ")
    c = float(split_line[0])
    f = float(split_line[1])
    x = float(split_line[2])

    amount_to_make = x - c
    ior = c/f

    time = 0
    production = 2
    while(True):
        time_to_reach_c = c / production
        time += time_to_reach_c
        
        
        time_to_reach_x = amount_to_make / production
        if (time_to_reach_x > ior):
            production += f
        else:
            time += time_to_reach_x
            return ("%.7f" % time)




def process_tests(command_to_run):
    
    out_file = open("out","w")
    number_of_tests = int(in_file.readline())
    for test_case in range(number_of_tests):
        test_string = in_file.readline()[:-1]
        test_answer = command_to_run(test_string)
        out_file.write("Case #" + str(test_case + 1) + ": " + str(test_answer) + "\n")
    out_file.close()
    in_file.close()
	
in_file = open('in')
process_tests(solve)
