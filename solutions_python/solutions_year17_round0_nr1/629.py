import sys


def parse(input_file):
    """Returns a iterable that elements are single test cases."""
    t = int(input_file.readline())
    for _ in range(t):
        pancakes, k = input_file.readline().strip().split()
        yield pancakes, int(k)


def solve(pancakes, k):
    """Main code."""
    is_ok = [c == '+' for c in pancakes]

    def flip(pos):
        for i in range(pos, pos + k):
            is_ok[i] = not is_ok[i]

    ans = 0
    for i in range(len(pancakes) - k + 1):
        if not is_ok[i]:
            flip(i)
            ans += 1
    return ans if all(is_ok) else "IMPOSSIBLE"


def save(answers, output_file):
    for i, answer in enumerate(answers):
        print("Case #{case_num}: {answer}".format(case_num=i+1, answer=answer), file=output_file)


def solve_all(input_file, output_file):
    answers = [solve(*case) for case in parse(input_file)]
    save(answers, output_file)


def main():
    if len(sys.argv) == 1:
        solve_all(sys.stdin, sys.stdout)
    else:
        input_file_name = sys.argv[1]
        output_file_name = input_file_name.replace(".in", ".out")
        with open(input_file_name) as input_file, open(output_file_name, "w") as output_file:
            solve_all(input_file, output_file)


if __name__ == '__main__':
    main()