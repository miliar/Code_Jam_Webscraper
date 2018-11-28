'''
Problem A. Standing Ovation
'''

#input_file = "2015_Q_A_small.in"
#input_file = "a_sample.txt"
input_file = "A-small-attempt0.in"

#output_file = "2015_Q_A_small_op.txt"
#output_file = "a_sample_out.txt"
output_file = "A-small-attempt0.out"

root = 0


def main_process(input_line):
    s_max , s_li = input_line.split(" ")
    s_max = int(s_max)
    s_list = []
    for c in str(s_li[:s_max+1]):
        s_list.append(int(c))
    print(s_max,"  " , s_list)

    res = 0

    for i in range(1,s_max+1):
        if i <= s_list[i-1]:
            s_list[i] = s_list[i] + s_list[i-1]
        else:
            res = res + 1
            s_list[i] = s_list[i] + s_list[i-1] + 1


    print("Res =", res)
    return res


if __name__ == '__main__':

    # Read and process the input file
    f1 = open(input_file, 'r')
    f2 = open(output_file, 'w')
    total_test_cases = int(f1.readline())

    for test_case in range(total_test_cases):
        input_line = f1.readline()
        res = main_process(input_line)
        op = 'Case #' + str(test_case + 1) + ': ' + str(res) + "\n"
        f2.write(op)

    print("Done")
    f1.close()
    f2.close()
