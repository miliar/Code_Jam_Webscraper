__author__ = 'Timo Hanisch'
__email__ = 'timohanisch@googlemail.com'

import sys


def standing_ovation(case_num, max_shyness, content):
    int_array = [int(content[i:(i + 1)]) for i in range(0, len(content))]
    standing_people = 0
    current_shyness_level = 0
    needed_friends = 0
    for current_shyness_people in int_array:
        if current_shyness_people > 0:
            if standing_people < current_shyness_level:
                needed_friends += (current_shyness_level - standing_people)
                standing_people += (current_shyness_level - standing_people)
            standing_people += current_shyness_people
        current_shyness_level += 1
    print "Case #" + str(case_num) + ": " + str(needed_friends)


def load_file_content(path):
    with open(path) as f:
        return [x.strip('\n') for x in f.readlines()]


if __name__ == '__main__':
    if len(sys.argv) - 1 <= 0:
        print "Wrong count of arguments!"
    else:
        file_path = sys.argv[1]
        file_content = load_file_content(file_path)
        test_cases = int(file_content[0])
        current_test_case = 1
        for line in file_content[1:]:
            max_shyness, content = line.split(" ")
            standing_ovation(current_test_case, max_shyness, content)
            current_test_case += 1