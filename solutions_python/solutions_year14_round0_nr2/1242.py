
file_name = "B-large.in"
out_file_name = "cookie.out"
out_file = open(out_file_name, 'w')

def cookies(case, C, F, X):
    base_rate = 2
    second_used = 0

    while (X / base_rate) > ((C / base_rate) + (X / (base_rate + F))):
        second_used += C / base_rate
        base_rate += F
    second_used += X / base_rate

    print_result(case, second_used)

def print_result(case, result):
    out_file.write("Case #" + str(case) + ": " + str(result) + '\n')

with open(file_name) as f:
    case_num = int(f.readline())
    for i in range(1, case_num + 1):
        line = f.readline().strip().split(' ')
        C = float(line[0])
        F = float(line[1])
        X = float(line[2])
        cookies(i, C, F, X)
