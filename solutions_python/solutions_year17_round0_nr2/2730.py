
def find_previous_tidy(last_number):
    string_output = int("".join([str(n) for n in last_number]))
    for i in range(0, len(last_number) - 1):
        if last_number[i] > last_number[i + 1]:
            for j in range(i + 1, len(last_number)):
                last_number[j] = 9
            last_number[i] -= 1
            return find_previous_tidy(last_number)
    return string_output

case = "B-Big"
output = ""

with open(case + ".in", "r") as fh:
    t = int(fh.readline().strip())
    for x in range(0, t):
        problem = list(fh.readline().strip())
        problem_ints = [int(s) for s in problem]
        result = str(find_previous_tidy(problem_ints))
        output += "Case #" + str(x+1) + ": " + result + "\n"

with open(case + ".out", "w") as fh:
    fh.write(output)
