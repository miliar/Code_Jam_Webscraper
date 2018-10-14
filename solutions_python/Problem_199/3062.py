import sys

SMILE = '+'
BLANK = '-'

sys.setrecursionlimit(3000)

class FlipException(Exception):
    pass


def flip(table, k, position):
    if position < 0 and abs(position) < k:
        position = -k
    return table[:position] + [SMILE if pancake == BLANK else BLANK for pancake in table[position:position+k]] + table[position+k:]


def step(table, k):
    #print(table)
    if check_win(table):
        return 0
    elif len(table) < k:
        raise FlipException
    else:
        if table[0] == BLANK:
            steps = step(flip(table, k, 0), k) + 1
        else:
            while table[0] == SMILE:
                table = table[1:]
            steps = step(table, k)
        return steps


def check_win(table):
    return all((pancake is SMILE for pancake in table))


def process(input, result_file):
    t = int(input[0])
    for i in range(1, t + 1):
        t, k = input[i].split(" ")
        k = int(k)

        try:
            steps = step(list(t), k)
        except FlipException:
            steps = -1

        result_string = "Case #{}: {}".format(i, steps if steps >= 0 else "IMPOSSIBLE")
        print(result_string)
        result_file.write(result_string + "\n")


if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    file_name = sys.argv[1]
    result_file_name = file_name + "_result"
    with open(result_file_name, 'w') as result_file:
        with open(file_name) as input_file:
            content = input_file.readlines()
        process(content, result_file)