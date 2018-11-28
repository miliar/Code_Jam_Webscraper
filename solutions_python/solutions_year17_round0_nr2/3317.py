
import sys


def tidyfi(nuMst):
    arr = [int(x) for x in list(nuMst)]

    if len(arr) == 1:
        return arr[0]

    pointer = findTidyPart(arr)

    if pointer == len(arr) - 1:
        return "".join([str(x) for x in arr])
    else:
        arr = tidy(pointer, arr)
        return "".join([str(x) for x in arr])


def tidy(pointer, arrI):
    # edge case
    if pointer == 0:

        if arrI[pointer] > 1:

            rest = [9 for _ in arrI[pointer + 1:]]
            temp = arrI[0: pointer + 1].copy()
            temp[0] -= 1
            temp.extend(rest)
            return temp

        else:
            temp = [9 for _ in arrI[pointer + 1:]]
            return temp

    # generic case

    rest = [9 for _ in arrI[pointer + 1:]]
    temp = arrI[0: pointer + 1].copy()
    counter = 1

    while counter < len(temp):

        if temp[-counter - 1] >= temp[- counter]:
            temp[-counter] = 9
            temp[-counter - 1] -= 1
            counter += 1

        else:
            temp[-counter] -= 1
            break

    temp.extend(rest)

    if temp[0] == 0:
        del (temp[0])

    return temp


def findTidyPart(arr):
    if len(arr) == 1:
        return 0

    for i in range(0, len(arr) - 1):
        if arr[i + 1] < arr[i]:
            return i

    return len(arr) - 1


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

        output_string = tidyfi(input_variable_array[0])

        fout.write("Case #"+str(test_case)+": "+ str(output_string) +"\n")

    fin.close()
    fout.close()


if __name__ == "__main__":
    main()
