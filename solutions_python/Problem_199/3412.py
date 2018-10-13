
def main():

    # file_name = "example.out"
    file_name = "A-small.out"
    # file_name = "A-large.out"

    try:

        # Open output file
        output_file = open(file_name, "w")

        # Read input data
        test_no = int(raw_input())

        # Process every test
        for it_t in range(test_no):

            line = raw_input().split(" ")
            pancakes = line[0]
            k = int(line[1])

            # transition_no = 0
            # current_symbol = ' '
            #
            # for pancake in pancakes:
            #     if pancake != current_symbol:
            #         transition_no += 1
            #         current_symbol = pancake
            #
            # transition_no -= 1

            temp = generate_config(len(pancakes), k)

            if pancakes not in temp:
                result = "IMPOSSIBLE"
            else:
                result = flipping(pancakes, k)

            output_file.write("Case #" + str(it_t + 1) + ": " + str(result))
            if it_t != test_no - 1:
                output_file.write("\n")

        # Close output file
        output_file.close()

    except IOError:
        print("Cannot open file " + str(file_name))

    except ValueError:
        print("Cannot convert number. ")


def flipping(pancakes, displ):

    print(pancakes)

    it = 0
    start = 0

    while pancakes[start] == '+':
        start += 1

        if start == len(pancakes):
            return it

    while pancakes != len(pancakes) * '+':
        print(pancakes)
        print(start)
        pancakes = make_config(pancakes, displ, start)
        it += 1

        while pancakes[start] == '+':
            start += 1

            if start == len(pancakes):
                return it

    return it


def check_config(config):

    if '+' in config and '-' in config:

        size = len(config)

        model1 = '+'
        for i in range(0, size - 1, 2):
            model1 += '-'
            model1 += '+'

        model2 = '-'
        for i in range(0, size - 1, 2):
            model2 += '+'
            model2 += '-'

        if config == model1 or config == model2:
            return True

    return False


def generate_config(char_no, displ):

    temp = [char_no * '+']

    for item in temp:
        for i in range(char_no - displ + 1):
            config = make_config(item, displ, i)

            if config not in temp:
                temp.append(config)

    # for item in temp:
    #     print(item)
    # print(len(temp))

    return temp


def make_config(scheme, displ, start):

    temp = ''
    for i in range(0, start):
        temp += scheme[i]

    for i in range(start, start + displ):
        if scheme[i] == '+':
            temp += '-'
        else:
            temp += '+'

    for i in range(start + displ, len(scheme)):
        temp += scheme[i]

    return temp


if __name__ == "__main__":

    # generate_config(7, 4)
    main()
