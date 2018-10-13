input_file = open('A-large.in', 'r')
input = input_file.readlines()
input_file.close()

n = input[0]
lines = input[1:]
case_number = 1
output_lines = []


def flip_pancakes(list, index, k):
    for i in range(k):
        if list[index + i] == 1:
            list[index + i] = 0
        else:
            list[index + i] = 1

for line in lines:
    row, k = line.split()
    k = int(k)
    pancake_list = []

    for pancake in row:
        if pancake == '-':
            pancake_list.append(0)
        else:
            pancake_list.append(1)

    n = len(pancake_list)
    flips = 0

    for index, pancake in enumerate(pancake_list):
        if pancake == 0 and (n - index) >= k:
            flip_pancakes(pancake_list, index, k)

            flips += 1
        elif pancake == 0:
            flips = -1
            break

    output_lines.append("Case #" + str(case_number) + ": " + (str(flips) if flips >= 0 else "IMPOSSIBLE") + "\n")
    case_number += 1

output_file = open('ouput', 'w')
output_file.writelines(output_lines)
output_file.close()

