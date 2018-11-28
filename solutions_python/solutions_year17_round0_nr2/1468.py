import unittest


def main():
    t_case = int(input())
    for i in range(t_case):
        inp_n = int(input())
        print("Case #{}: {}".format(i + 1, solve(inp_n)))


def solve(num):
    while True:
        num_lst = num_to_lst(num)
        pos = first_un_tidy_pos(num_lst)
        if pos is None:
            return num
        num_lst[pos] = (10 + num_lst[pos] - 1) % 10
        for i in range(pos + 1, len(num_lst)):
            num_lst[i] = 9
        num = lst_to_num(num_lst)


def is_tidy_num(num):
    num_lst = num_to_lst(num)
    if first_un_tidy_pos(num_lst) is None:
        return True
    return False


def lst_to_num(lst_num):
    return int(''.join(map(str, lst_num)))


def num_to_lst(num):
    return [int(i) for i in str(num)]


def first_un_tidy_pos(num_lst):
    for i in range(len(num_lst) - 1):
        if num_lst[i] > num_lst[i + 1]:
            return i
    return None


if __name__ == "__main__":
    import sys

    sys.stdin = open("B-large.in", 'r')
    sys.stdout = open("temp.out", 'w')
    main()


class TestMethods(unittest.TestCase):
    def test_is_tidy_num(self):
        self.assertEqual(is_tidy_num(1234), True)
        self.assertEqual(is_tidy_num(1211), False)
        self.assertEqual(is_tidy_num(132), False)
        self.assertEqual(is_tidy_num(99), True)
        self.assertEqual(is_tidy_num(3), True)

    def test_solve(self):
        self.assertEqual(solve(12341012341234), 12339999999999)
        self.assertEqual(solve(111111111111111110), 99999999999999999)
        self.assertEqual(solve(132), 129)
        self.assertEqual(solve(1000), 999)
        self.assertEqual(solve(7), 7)

    def test_lst_to_num(self):
        self.assertEqual(lst_to_num([1, 2, 3]), 123)
        self.assertEqual(lst_to_num([0, 9, 0]), 90)
        self.assertEqual(lst_to_num([9]), 9)

    def test_num_to_lst(self):
        self.assertEqual(num_to_lst(2134), [2, 1, 3, 4])

    def test_first_un_tidy_pos(self):
        self.assertEqual(first_un_tidy_pos([1, 2, 3, 4]), None)
        self.assertEqual(first_un_tidy_pos([1, 1, 0, 1]), 1)
