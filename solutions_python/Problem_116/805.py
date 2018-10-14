import operator

out_msg = {"O": "O won",
"X": "X won","D": "Draw","N": "Game has not completed"}

# read
def file_read(input_file, output_file, out_msg):
    with open(input_file, "r") as fin:
        with open(output_file, "w") as fout:
            num_test_cases = int(fin.readline())
            for i in range(num_test_cases):
                winner = findout_winner([fin.readline().rstrip() for j in range(4)])
                print winner
                fout.write("Case #{num}: {msg}\n".format(num=i+1, msg=out_msg.get(winner)))
                fin.readline()

file_read("A-large.in", "out.txt", out_msg)

def is_line(four_letters):
    O = [i for i in four_letters if i == 'O']
    X = [i for i in four_letters if i == 'X']
    T = [i for i in four_letters if i == 'T']
    if(len(four_letters) == len(O) + len(T)):
        return 'O'
    if(len(four_letters) == len(X) + len(T)):
        return 'X'
    return None


line_pos = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [0, 5, 10, 15], [12, 9, 6, 3]]

def findout_winner(four_strings):
    whole_list = "".join(four_strings)
    var_is_line = None
    for line in line_pos:
        line_getter = operator.itemgetter(*line)
        var_is_line = is_line(list(line_getter(whole_list)))
        if var_is_line is not None:
            return var_is_line
    # check if draw or not yet
    if not "." in whole_list:
        return "D"
    else:
        return "N"
