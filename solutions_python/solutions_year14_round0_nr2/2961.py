__author__ = 'basit'

file_input = open("cookie_clicker.in")
file_output = open("cookie_clicker.out", "w")

# initialization input
num_of_cases = int(file_input.readline())

for case in xrange(num_of_cases):
    C, F, X = [float(x) for x in file_input.readline().split()]

    time_taken = 0
    current_production = 2.0

    while True:
        time_to_reach_c = C / current_production
        time_to_reach_x = X / current_production
        time_to_reach_x_with_c = time_to_reach_c + (X / (current_production + F))

        # print time_to_reach_c, time_to_reach_x, time_to_reach_x_with_c

        if time_to_reach_x < time_to_reach_x_with_c:
            time_taken += time_to_reach_x
            break
        else:
            time_taken += time_to_reach_c
            current_production += F

    if case > 0:
        print "\n"
        file_output.write("\n")

    print "Case #%d: %s" % (case + 1, time_taken)
    file_output.write("Case #%d: %s" % (case + 1, time_taken))

file_output.close()
