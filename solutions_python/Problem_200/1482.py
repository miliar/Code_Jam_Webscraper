import sys

def read_data(filename):
    with open(filename) as f:
        cases = int(f.readline().strip())
        data = []
        for i in xrange(cases):
            number = f.readline().strip()
            data.append(map(int, list(number)))
        return data

def last_tidy(data):
    case_num = 1
    for number in data:
        index = len(number) - 1
        min_number = number[-1]
        while index > 0:
            if number[index] < number[index - 1]:
                number[index] = 9
                number[index - 1] -= 1
            new_min_number = max(*number[index - 1:index + 1])
            if new_min_number > min_number:
                # Just raise the tailing numbers to min_number (is going to be 9)
                for index2 in range(index, len(number)):
                    number[index2] = new_min_number
            min_number = new_min_number

            index -= 1

        print "Case #{}: {}".format(case_num, int(''.join(map(str, number))))
        case_num += 1


if __name__ == '__main__':
    file_name = sys.argv[1]

    last_tidy(read_data(file_name))
