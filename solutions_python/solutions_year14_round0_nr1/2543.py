import time
import datetime

__author__ = 'eegee'

filename = "A-small-attempt0"

input_data = open("../data/" + filename + ".in")
output_data = open("../data/" + filename + ".out", "w")
time.perf_counter()

for case in range(1, int(input_data.readline()) + 1):
    answer = ""
    # read inputs #
    response1 = int(input_data.readline())
    cards1 = {1: set(map(int, input_data.readline().split())),
              2: set(map(int, input_data.readline().split())),
              3: set(map(int, input_data.readline().split())),
              4: set(map(int, input_data.readline().split()))}
    response2 = int(input_data.readline())
    cards2 = {1: set(map(int, input_data.readline().split())),
              2: set(map(int, input_data.readline().split())),
              3: set(map(int, input_data.readline().split())),
              4: set(map(int, input_data.readline().split()))}
    # read inputs #

    # solution #
    common = cards1[response1] & cards2[response2]
    if len(common) == 0:
        answer = "Volunteer cheated!"
    elif len(common) == 1:
        answer = str(common.pop())
    else:
        answer = "Bad magician!"
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