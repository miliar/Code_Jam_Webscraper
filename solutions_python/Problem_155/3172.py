import os
def read_input(filename):
    num_test_cases = 0
    tests = []
    with open(os.path.abspath(filename)) as infile:
        for line_number, line in enumerate(infile):
            if line_number == 0:
                num_test_str = line.strip()
                num_test_cases = int(num_test_str)
            else:
                tests.append((line.strip(), line_number))

    return tests

def get_num_friends(test):
    shyness_list = []
    test_strings = test.split(" ")
    if len(test_strings) > 1:
        max_shyness_level = test_strings[0]
        shyness_string = test_strings[1]
    else:
        shyness_string = test

    for shyness_level, num_str in enumerate(shyness_string):
        shyness_list.append((shyness_level, int(num_str)))

    people_standing = 0
    friends_added = 0
    for shyguy in shyness_list:
        shyness_level, num_people = shyguy
        if shyness_level == 0:
            people_standing = num_people
        else:
            if people_standing >= shyness_level:
                people_standing+= num_people

        while people_standing <= shyness_level:
            people_standing+=1
            friends_added+=1
    return friends_added


def write_output(out_string):
    with open("output.txt", 'wt') as outfile:
        outfile.write(out_string)


def main():
    file_path = "A-large.in"
    tests = read_input(file_path)
    out_string = ""
    for test in tests:
        friends_added = get_num_friends(test[0])
        out_string += "Case #{}: {}\n".format(test[1], friends_added)

    write_output(out_string)

if __name__ == "__main__":
    main()