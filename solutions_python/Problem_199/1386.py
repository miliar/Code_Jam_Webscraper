import unittest


def is_solved(inp_str):
    return len(list(filter(lambda x: x != "+", inp_str))) == 0


def flip_cake(cake):
    if cake == "+":
        return "-"
    elif cake == "-":
        return "+"
    return None


def flip_lst_cake(inp_str, k, pos):
    inp_lst = list(inp_str)
    for i in range(pos, min(len(inp_str), pos + k)):
        inp_lst[i] = flip_cake(inp_lst[i])
    return ''.join(inp_lst)


def solve(inp_str, k):
    l = len(inp_str)
    ans = 0
    for i in range(l - k + 1):
        if inp_str[i] == "-":
            inp_str = flip_lst_cake(inp_str, k, i)
            ans += 1
    if is_solved(inp_str):
        return ans
    return None


def main():
    t_case = int(input())
    for i in range(t_case):
        inp_str, k = input().split()
        k = int(k)
        ans = solve(inp_str, k)
        print("Case #{}: {}"
              .format(i + 1, ans if ans is not None else "IMPOSSIBLE"))


if __name__ == "__main__":
    import sys
    sys.stdin = open("A-large.in", 'r')
    sys.stdout = open("out", 'w')
    main()


class TestMethods(unittest.TestCase):
    def test_is_solved(self):
        self.assertEqual(is_solved("+++++"), True)
        self.assertEqual(is_solved("++-++++"), False)

    def test_flip_cake(self):
        self.assertEqual(flip_cake("+"), "-")
        self.assertEqual(flip_cake("-"), "+")

    def test_flip_lst_cake(self):
        self.assertEqual(flip_lst_cake("++-+++", 3, 0), "--++++")
        self.assertEqual(flip_lst_cake("++-+++", 3, 1), "+-+-++")

    def test_solve(self):
        self.assertEqual(solve("---+-++-", 3), 3)
        self.assertEqual(solve("+++++", 4), 0)
        self.assertEqual(solve("-+-+-", 4), None)
        self.assertEqual(solve("++---", 3), 1)
