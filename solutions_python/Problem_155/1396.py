import sys

def solve(input):
    line = input.split()
    total_number_of_audience = int(line[0])

    current_total = 0
    additional_audience = 0
    for index, char in enumerate(line[1]):
        shyness_level = index
        number_of_audience = int(char)
        additional_audience_now = 0

        if current_total < shyness_level:
            additional_audience_now = shyness_level - current_total
            additional_audience = additional_audience + additional_audience_now

        current_total = current_total + number_of_audience + additional_audience_now

    return additional_audience


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as input:
        T = int(input.readline())
        for case in range(0, T):
            output = solve(input.readline())
            print "Case #%d: %s" % (case + 1, output)
