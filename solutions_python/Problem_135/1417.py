import sys
from collections import Counter
import itertools
from pprint import pprint

def write_output(output):
    lines = []
    for i, out in enumerate(output):
        line = 'Case #{}: {}'.format(i + 1, out)
        lines.append(line)

    txt = '\n'.join(lines) + '\n'
    with open(r'C:\codejam\output.txt', 'w') as f:
        f.write(txt)


def process(answer1, rows1, answer2, rows2):
    row1 = rows1[answer1 - 1]
    row2 = rows2[answer2 - 1]

    nums = set(row1).intersection(row2)
    if len(nums) == 1:
        return nums.pop()
    elif len(nums) == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'


def main():
    output = []

    filepath = sys.argv[1]
    with open(filepath, 'r') as f:
        num_cases = int(f.readline().strip())
        for i in range(num_cases):
            answer1 = int(f.readline().strip())
            rows1 = [map(int, f.readline().strip().split()) for j in range(4)]

            answer2 = int(f.readline().strip())
            rows2 = [map(int, f.readline().strip().split()) for j in range(4)]

            output.append(process(answer1, rows1, answer2, rows2))

    write_output(output)


if __name__ == '__main__':
    main()