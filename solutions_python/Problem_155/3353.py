

def main():

    f = open('input.txt', 'r')

    cases = int(f.readline())
    cases = 1
    for line in f:
        minimum = get_minimum(line)
        print "Case #{}: {}".format(cases, minimum)
        cases +=1


def get_minimum(line):

    max_shyness, people = line.split(" ")
    return quackulate(people[:int(max_shyness)])


def quackulate(line):
    sum = 0
    digit = 1
    min = 0
    for number in line:
        sum = sum + int(number)
        if sum < digit:
            min += 1
            sum += 1
        digit += 1

    return min


if __name__ == "__main__":
    main()
