import unittest


def get_level_distribution(line):
    return int(line.split()[0]), line.split()[1]


input_file = open('../resources/prob1/A-large.in', 'r')
number_of_tests = input_file.readline()

result_file = open("../resources/prob1/A-large.out", "w")


def calculate_guest_to_add(shiness_level, distribution):
    guest_to_add = 0
    clappers = 0
    for i in range(int(shiness_level)+1):
        if int(distribution[i]) and clappers + guest_to_add < i:
            guest_to_add += i - (clappers + guest_to_add)
        clappers += int(distribution[i])

    return guest_to_add


for j in range(int(number_of_tests)):
    shiness_lv, distr = get_level_distribution(input_file.readline())
    print "{}, {}".format(shiness_lv, distr)

    result_file.write("Case #{}: {}\n".format(j + 1, calculate_guest_to_add(shiness_lv, distr)))

input_file.close()
result_file.close()


class MyTestCase(unittest.TestCase):

    def test_calculate_guest_to_add(self):
        self.assertEqual(calculate_guest_to_add('4', '11111'), 0)
        self.assertEqual(calculate_guest_to_add('1', '09'), 1)
        self.assertEqual(calculate_guest_to_add('5', '110011'), 2)
        self.assertEqual(calculate_guest_to_add('0', '1'), 0)
        self.assertEqual(calculate_guest_to_add('5', '120061'), 1)
        self.assertEqual(calculate_guest_to_add('5', '120061'), 1)


if __name__ == '__main__':
    unittest.main()
