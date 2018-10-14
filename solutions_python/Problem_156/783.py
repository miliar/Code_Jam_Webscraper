import unittest


def get_level_distribution(line):
    return int(line.split()[0]), line.split()[1]


input_file = open('B-small-attempt3.in', 'r')
number_of_tests = input_file.readline()

result_file = open("B-small-attempt3.out", "w")


# Retrieve data and output result
def calculate_time(number_of_plates, pancakes_distribution):
    pancakes_distribution.sort(reverse=True)
    min_time = pancakes_distribution[0]
    special_minutes = 0
    while pancakes_distribution[0] > 3:
        # split bigger and...
        if (pancakes_distribution[0] == 9 and len(pancakes_distribution) == 1) or \
                (len(pancakes_distribution) > 1 and pancakes_distribution[0] == 9 and (pancakes_distribution[1] <= 3 or pancakes_distribution[1] == 6)):
            pancakes_distribution.append(6)
            pancakes_distribution.append(3)
            pancakes_distribution.pop(0)
            pancakes_distribution.sort(reverse=True)
        else:
            pancakes_distribution.append(pancakes_distribution[0] / 2)
            pancakes_distribution.append(pancakes_distribution[0] / 2 + pancakes_distribution[0] % 2)
            pancakes_distribution.pop(0)
            pancakes_distribution.sort(reverse=True)
        # ...add minute
        special_minutes += 1
        # ...and update min_time if got lower
        if pancakes_distribution[0] + special_minutes < min_time:
            min_time = pancakes_distribution[0] + special_minutes

    return min_time


for j in range(int(number_of_tests)):
    number_of_plates = int(input_file.readline())
    pancakes_distribution = list(input_file.readline().replace(" ", ""))
    if pancakes_distribution[-1] == '\n':
        pancakes_distribution = pancakes_distribution[:-1]
    pancakes_distribution = [int(p) for p in pancakes_distribution]
    print "{}, {}".format(number_of_plates, pancakes_distribution)
    time = calculate_time(number_of_plates, pancakes_distribution)
    print "Case #{}: {}\n".format(j + 1, time)
    result_file.write("Case #{}: {}\n".format(j + 1, time))

input_file.close()
result_file.close()


class MyTestCase(unittest.TestCase):

    def test_calculate_guest_to_add(self):
        self.assertEqual(calculate_time(1, [3]), 3)
        self.assertEqual(calculate_time(4, [1, 2, 1, 2]), 2)
        self.assertEqual(calculate_time(1, [4]), 3)
        self.assertEqual(calculate_time(2, [9, 3]), 5)
        self.assertEqual(calculate_time(3, [9, 3, 2]), 5)
        self.assertEqual(calculate_time(3, [9, 4, 3]), 6)
        self.assertEqual(calculate_time(1, [9]), 5)
        self.assertEqual(calculate_time(2, [9, 9]), 7)
        self.assertEqual(calculate_time(2, [8, 2]), 5)
        self.assertEqual(calculate_time(4, [9, 9, 9, 8]), 9)
        self.assertEqual(calculate_time(2, [9, 6]), 6)

if __name__ == '__main__':
    unittest.main()