import operator
import math
def find_ans(down, up):
    down_sqrt = math.sqrt(down)
    down_sqrt = int(down_sqrt) if down_sqrt == int(down_sqrt) else int(down_sqrt) + 1
    up_sqrt = int(math.sqrt(up))
    ans = 0
    for i in range(down_sqrt, up_sqrt+1):
        if is_fair(i) and is_fair(i*i):
            ans = ans + 1
    return ans
def is_fair(int_n):
    str_n = str(int_n)
    return str_n == str_n[::-1]

# read
def file_read(input_file, output_file):
    with open(input_file, "r") as fin:
        with open(output_file, "w") as fout:
            num_test_cases = int(fin.readline())
            for i in range(num_test_cases):
                xy = fin.readline().rstrip().split()
                x = int(xy[0])
                y = int(xy[1])
                ans = find_ans(x, y)
                fout.write("Case #{num}: {msg}\n".format(num=i+1, msg=ans))


file_read("C-small-attempt0.in", "out_c.txt")




