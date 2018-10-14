def solve(answer_a, square_a, answer_b, square_b):
    result = -1
    for item in square_a[answer_a - 1]:
        if item in square_b[answer_b - 1]:
            if result == -1:
                result = item
            else:
                result = "Bad magician!"
    if result == -1:
        result = "Volunteer cheated!"
    return result

file_in = open("A-small-attempt2.in", "r")
#file_in = open("in.txt", "r")
file_out = open("out.txt", "w")

n_case = int(file_in.readline())

for case_index in range(0, n_case):
    answer_a = int(file_in.readline())
    square_a = []
    square_b = []
    for i in range(4):
        square_a.append(file_in.readline().strip().split(" "))
    answer_b = int(file_in.readline())
    for i in range(4):
        square_b.append(file_in.readline().strip().split(" "))
    result = solve(answer_a, square_a, answer_b, square_b)
    file_out.write("Case #%d: %s\n" % (case_index + 1, result))

file_out.close()
file_in.close()
