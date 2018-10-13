import time
import datetime
from builtins import print

__author__ = 'eegee'

filename = "B-large"

input_data = open("../data/" + filename + ".in")
output_data = open("../data/" + filename + ".out", "w")
time.perf_counter()

for case in range(1, int(input_data.readline()) + 1):
    answer = ""
    # read inputs #
    farm_cost, additional_cps, cookies_needed = list(map(float, input_data.readline().split()))
    # read inputs #

    # solution #
    current_cps = 2
    seconds_passed = 0
    current_projection = best_projection = float('inf')

    while current_projection <= best_projection:
        best_projection = current_projection
        current_projection = seconds_passed + (cookies_needed / current_cps)
        seconds_passed += farm_cost / current_cps
        current_cps += additional_cps

    answer = "{:.7f}".format(best_projection)
    # solution #

    # display and write output #
    output_line = "Case #" + str(case) + ": "
    print(output_line + answer)
    output_data.write(output_line + answer + "\n")
    # display and write output #

print()
print("total_time:", datetime.timedelta(seconds=time.perf_counter()))
input_data.close()
output_data.close()