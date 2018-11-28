

def solve_case(ggs_count, s, p, input_line_parts):

    result = 0

    gg_index = 3
    while gg_index < ggs_count+3:

        total = int(input_line_parts[gg_index])

        a = total/3
        t = total%3

        if total == 0:
            r = [0, 0]
        elif t == 0:
            r = [a, a+1]
        elif t == 1:
            r = [a+1, a+1]
        else:
            r = [a+1, a+2]


        if r[0] >= p:
            result += 1
        else:
            if (r[1] >= p) and (s > 0):
                result += 1
                s -= 1

        gg_index += 1

    return result

input_file = open("input.txt", "r")
input_lines_count = int(input_file.readline())
line_index = 0

result = ''
while line_index < input_lines_count:
    input_line = input_file.readline()
    input_line_parts = input_line.split(" ")
    t = int(input_line_parts[0])
    s = int(input_line_parts[1])
    p = int(input_line_parts[2])

    line_no = line_index + 1
    result += "Case #" + str(line_no) + ": " + str(solve_case(t, s, p, input_line_parts)) + "\n"
    line_index += 1


output_file = open("result.txt", "w")
output_file.writelines(result)
output_file.close()

