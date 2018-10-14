import sys


def main(argv=None):
    if argv is None:
        argv = sys.argv


    filename = 'BLarge'
    output = open(filename + '_output.txt', 'w')

    with open(filename + '.txt') as file:
        t = int(file.readline())
        input = file.readlines()
        input[-1] += '\n'
        input = list(map(lambda x: x[:-1], input))

        count = 1
        for index in input:
            i_str = index
            i_num = int(index)
            found = False
            while not found:

                if i_str == "".join(sorted(i_str)):
                    output.write('Case #{}: {}\n'.format(count, i_str))
                    found = True
                    break

                substract = calculate_substraction(i_str)
                i_num -= substract
                i_str = str(i_num)
            count += 1

    output.close()

def calculate_substraction(number_str):
    for j in range(0, len(number_str)):
        for k in range(j + 1, len(number_str)):
            if number_str[j] > number_str[k]:
                return (int(number_str[k:]) + 1)

if __name__ == "__main__":
    sys.exit(main())