def readFile(filename, mode="rt"):
    with open(filename, mode) as fin:
        return fin.read()

def writeFile(filename, contents, mode="wt"):
    with open(filename, mode) as fout:
        fout.write(contents)

def get_min_friends(s_max, levels_array):
    num_people_standing = 0
    friends_to_add = 0
    for shyness_level in xrange(0, int(s_max) + 1):
        num_people = int(levels_array[shyness_level])
        while num_people_standing < shyness_level:
            friends_to_add += 1
            num_people_standing += 1
        num_people_standing += num_people
    return friends_to_add

def main():
    file_text = readFile("gcj_in.txt")
    file_lines = file_text.splitlines()

    ##### Implementation START

    num_test_cases = int(file_lines[0])
    output_string = ""

    for case_num in xrange(1, num_test_cases + 1):
        line_args = file_lines[case_num].split(" ");
        s_max = line_args[0];
        levels_array = list(line_args[1])

        min_friends = get_min_friends(s_max, levels_array)

        output_string += "Case #%i: %i" % (case_num, min_friends)
        if (case_num < num_test_cases): output_string += "\n"

    ##### Implementation END

    writeFile("gcj_out.txt", output_string)

if __name__ == "__main__":
    main()
