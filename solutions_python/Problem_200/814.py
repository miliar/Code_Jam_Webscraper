import sys
from collections import defaultdict

def main():

    #  reading in the arguments of the code executable
    fin_name = sys.argv[1]
    fout_name = sys.argv[2]

    digits = defaultdict(list)

    for digit in range(0,10):
        digits[str(digit)] = str((digit-1)%10)

    # opening the output file for writing
    fout = open(fout_name, 'w')

    #  reading all lines at once from the opened file
    with open(fin_name, 'r') as fin:
        lines = fin.readlines()

    # T - number of test casess
    T = int(lines[0].split()[0])

    for test_case in range(1, T+1):
        number = lines[test_case].split()[0]
        if len(number) == 1:
            output_string = number
        else:
            output_string = get_nearest_non_decreasing(number,digits)

        fout.write("Case #"+str(test_case)+": "+output_string+"\n")

    fin.close()
    fout.close()

def get_nearest_non_decreasing(number, digits):

    string_length = len(number)
    index = 0
    index_trailing = 0

    while (number[index] <= number[index+1]) :
        index += 1
        if number[index-1] != number[index]:
            index_trailing = index
        if index == string_length - 1:
            break

    if (index == string_length - 1):
        return number

    else:
        if number[index] == "1":
            return "9"*(string_length-1)
        else:
            prefix = number[0:index_trailing] + digits[number[index]]

            return prefix + "9"*(string_length-index_trailing-1)



if __name__ == "__main__":
    main()
