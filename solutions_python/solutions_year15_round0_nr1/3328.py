
def gen_list(test_input):
    """
    Returns a list of integers split from the string
    :param test_input:
    :return: A list of numbers
    """
    split_str = list(test_input)
    split_str = [int(i) for i in split_str]

    return split_str

def frnds_needed(max_people):
    """
    Calculates people invited so far.
    Compares it to see if shyness level is met
    Returns no. of people to be invited
    :param max_people:
    :return:
    """
    clap_counter = range(len(max_people))
    #print(clap_counter)
    ppl_so_far = 0
    invite = 0

    for clap in clap_counter:
        ppl_so_far += max_people[clap]
        if ppl_so_far > (len(max_people) - 1):
            return invite
        while ppl_so_far <= clap:
            if clap == 0 and ppl_so_far == 0:
                invite += 1
                ppl_so_far += 1
            else:
                invite += 1
                ppl_so_far += 1

    return invite

def main():
    min_frnds = 0

    # Open test file
    test_file = open("/Users/Anish_Bivalkar/Desktop/Hangman/CodeJam/input.in")
    test_file.readline()

    test_case = 1
    new_file = open("/Users/Anish_Bivalkar/Desktop/Hangman/CodeJam/output.in", "w")

    for line in test_file.readlines():

        new_line = line.split(" ")

        # Length of threshold = max_clappers
        converter = gen_list(new_line[1].strip())
        min_frnds = frnds_needed(converter)

        output = ("Case #" + str(test_case) + ": " + str(min_frnds) + "\n")
        print(output)
        new_file.write(output)
        test_case += 1

    new_file.close()
    test_file.close()

if __name__ == '__main__':
    main()