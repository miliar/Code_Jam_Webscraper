import datetime
import time

__author__ = 'eegee'

filename = "A-large"

input_data = open("../data/" + filename + ".in")
output_data = open("../data/" + filename + ".out", "w")
time.perf_counter()

for case in range(int(input_data.readline())):
    # read inputs #
    pancakes, flip_size = input_data.readline().split()
    pancakes = list(pancakes)
    flip_size = int(flip_size)
    # read inputs #

    flip = {"+": "-", "-": "+"}

    # solution #
    if flip_size % 2 == 0 and pancakes.count("-") % 2 != 0:
        answer = "IMPOSSIBLE"
    else:
        flips = 0
        for i, pancake in enumerate(pancakes):
            if (pancakes.count("-") == 0) or (i + flip_size) > len(pancakes):
                break
            if pancake == "-":
                pancakes[i:i + flip_size] = map(lambda c: flip[c], pancakes[i:i + flip_size])
                flips += 1
        if pancakes.count("-") == 0:
            answer = flips
        else:
            answer = "IMPOSSIBLE"
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
