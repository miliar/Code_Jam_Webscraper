import time
import datetime
__author__ = 'eegee'

filename = "A-large"

input_data = open("../data/" + filename + ".in")
output_data = open("../data/" + filename + ".out", "w")
time.perf_counter()

for case in range(int(input_data.readline())):
    answer = ""
    # read inputs #
    max_shyness, shy_levels = input_data.readline().split()
    max_shyness = int(max_shyness)
    shy_levels = list(shy_levels)
    # read inputs #

    # solution #
    count = 0
    friends_needed = 0
    for i in range(max_shyness + 1):
        count += int(shy_levels[i])
        if count <= i:
            friends_needed += 1
            count += 1
    answer = friends_needed
    # solution #

    # display and write output #
    output_line = "Case #" + str(case + 1) + ": "
    print(output_line + str(answer))
    output_data.write(output_line + str(answer) + "\n")
    # display and write output #

print()
print("total_time:", datetime.timedelta(seconds=time.perf_counter()))
input_data.close()
output_data.close()