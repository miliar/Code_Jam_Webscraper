import sys
import itertools


def find_forward(row):
    for char in row:
        if char != '?':
            return char

def process(input, result_file):
    t = int(input[0])
    last = 1
    for i in range(1, t + 1):
        #print("rc", input[last])
        r, c = input[last].split(" ")
        r, c = int(r), int(c)
        cake = input[last+1:last+r+1]
        cake = [list(row) for row in cake]
        last += r+1
        #print(cake)
        result = ""

        ## do work here
        again = False
        for row_i in range(len(cake)):
            last_char = '?'
            for col_i in range(len(cake[row_i])):
                if cake[row_i][col_i] == '?':
                    if col_i == 0:
                        last_char = find_forward(cake[row_i])
                    cake[row_i][col_i] = last_char

                    if last_char == '\n':
                        if again or row_i == 0:
                            again = True
                        else:
                            cake[row_i] = cake[row_i-1]
                elif cake[row_i][col_i] != '\n':
                    last_char = cake[row_i][col_i]

                    if again:
                        for row_j in range(row_i):
                            cake[row_j] = cake[row_i]
                        again = False
        #print(cake)
        # if again:
        #     if
        #     pass # check rows

        result_string = "Case #{}:\n{}".format(i, ''.join(itertools.chain.from_iterable(cake)))
        print(result_string)
        result_file.write(result_string )

if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "testinput"

    result_file_name = file_name + "_result"
    with open(result_file_name, 'w') as result_file:
        with open(file_name) as input_file:
            content = input_file.readlines()
        process(content, result_file)