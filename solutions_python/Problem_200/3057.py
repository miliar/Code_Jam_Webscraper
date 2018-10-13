import datetime
import time

__author__ = 'eegee'

filename = "B-large"

input_data = open("../data/" + filename + ".in")
output_data = open("../data/" + filename + ".out", "w")
time.perf_counter()

for case in range(int(input_data.readline())):
    # read inputs #
    n_chars = list(input_data.readline().strip())
    # read inputs #

    answer = []
    # solution #
    if len(n_chars) == 1:
        answer = n_chars[0]
    else:
        for i, n_char in enumerate(n_chars):
            if i == len(n_chars) - 1:
                answer.append(n_char)
            elif int(n_char) <= int(n_chars[i + 1]):
                answer.append(n_char)
            else:
                answer.append(str(int(n_char) - 1))
                answer.append("9" * (len(n_chars) - i - 1))
                while i > 0:
                    i -= 1
                    if int(answer[i]) > int(answer[i + 1]):
                        answer[i] = (str(int(answer[i]) - 1))
                        answer[i + 1] = "9"
                break
    # solution #
    # answer = "".join(answer)
    answer = int("".join(answer))

    # display and write output #
    output_line = "Case #" + str(case + 1) + ": "
    print(output_line + str(answer))
    output_data.write(output_line + str(answer) + "\n")
    # display and write output #

print()
print("total_time:", datetime.timedelta(seconds=time.perf_counter()))
input_data.close()
output_data.close()
