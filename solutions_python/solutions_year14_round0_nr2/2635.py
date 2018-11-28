import sys
import fileinput

test_case = 0
result = []
msg = 'Case #{test}: {sec:.7f}'

number_of_test_case = None

for line in fileinput.input():
    if fileinput.isfirstline():
        number_of_test_case = int(line)
        continue
    test_case += 1

    if test_case > number_of_test_case:
        break

    numbers = line.split()
    C = float(numbers[0])
    F = float(numbers[1])
    X = float(numbers[2])

    K = 2.0
    SEC = C / K
    COOKIES = C

    if C > X:
        result.append(msg.format(test=test_case, sec=X/K))
        continue

    while True:
        normal_sec = (X - COOKIES) / K
        speed_sec = X / (K + F)
        if speed_sec < normal_sec:
            K += F
            SEC += C / K
            COOKIES = C
        else:
            SEC += normal_sec
            break

    result.append(msg.format(test=test_case, sec=SEC))


print '\n'.join(result)
