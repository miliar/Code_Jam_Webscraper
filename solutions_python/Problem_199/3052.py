import sys


def pancakes(k, st):
    arr = list(st)

    try:
        pointer = arr.index("-")
    except ValueError:
        return "0"

    flipNumber = 0

    while True:
        try:
            pointer = arr.index("-")
            arr = arr[pointer:]

            if len(arr) >= k:
                flipPancakes(k, arr)
                flipNumber += 1
            else:
                return "IMPOSSIBLE"

        except ValueError:
            return str(flipNumber)



def flipPancakes(k, arr):
    for i in range(k):
        arr[i] = plusMinus(arr[i])


def plusMinus(ch):
    if ch == "+":
        return "-"
    else:
        return "+"


def main():

    #  reading in the arguments of the code executable
    fin_name = sys.argv[1]
    fout_name = sys.argv[2]

    # opening the output file for writing
    fout = open(fout_name, 'w')

    #  reading all lines at once from the opened file
    with open(fin_name, 'r') as fin:
        lines = fin.readlines()

    # T - number of test casess
    T = int(lines[0].split()[0])

    for test_case in range(1, T+1):
        input_variable_array = lines[test_case].split()

        output_string = pancakes(int(input_variable_array[-1]), input_variable_array[0])


        fout.write("Case #" + str(test_case) + ": " + output_string + "\n")

    fin.close()
    fout.close()


if __name__ == "__main__":
    main()
