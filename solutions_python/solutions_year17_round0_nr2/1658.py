
import sys



def is_tidy(x):
    previous = x[0]
    for item in x[1:]:
        if item < previous:
            return False
        previous = item
    return True


def clean_up(x):
    if is_tidy(x):
        return ''.join(map(str, x))

    # Forward pass to find first inflection point
    for i in range(1, len(x)):
        if x[i] < x[i - 1]:
            inflection = i
            break

    y = x[:inflection]
    y[inflection-1] -= 1
    for i in range(len(y) - 1, 0, -1):
        if y[i] < y[i - 1]:
            y[i] = 9
            y[i - 1] = y[i - 1] - 1
        else:
            # y[i] = y[i] - 1
            return ''.join(map(str, y)) + '9' * (len(x) - inflection)
    if y[0] == 0:
        y = y[1:]
    print(inflection)
    print(len(x))
    return ''.join(map(str, y)) + '9' * (len(x) - inflection)


if __name__ == '__main__':

    for arg in sys.argv:
        inputfilename = arg

    # check if input string is null???

    inputfile = open(inputfilename, 'r')

    outputfile = open(inputfilename + ".out", 'w')
    numberofsets = int(inputfile.readline())

    for m in range(numberofsets):
        x = inputfile.readline().rstrip('\r\n')
        x = [int(i) for i in x]
        print(x)
        # print(is_tidy(x))
        result = clean_up(x)
        # print(result)

        outputline = "Case #" + str(m + 1) + ": " + result + "\n"
        print(outputline)
        outputfile.write(outputline)
