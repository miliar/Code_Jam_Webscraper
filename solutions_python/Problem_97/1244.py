import sys


def solve_line(line_num, line):
    result = 0
    found_ones = {}

    nums = line.split(' ')
    A = int(nums[0])
    B = int(nums[1])

    for i in range(A, B + 1):
        digits = list(str(i))
        shifted_perms = []

        for j in range(1, len(digits)):
            shifted_perms.append(digits[-j:] + digits[:-j])

        for perm in shifted_perms:
            num = int(''.join(perm))

            if num == i:
                continue

            if A <= num <= B:
                if i < num:
                    k = i
                    v = num
                else:
                    k = num
                    v = i

                if k in found_ones:
                    if v in found_ones[k]:
                        continue

                if k not in found_ones:
                    found_ones[k] = [v]
                else:
                    found_ones[k].append(v)

                result += 1

    return result


def process_results(results):
    with open('problem_c_solution.txt', 'w') as f:
        for i, r in enumerate(results):
            f.write('Case #%d: %s\n' % (i + 1, r))


def main():
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        lines = f.readlines()
        lines = lines[1:]

        results = []

        for i, line in enumerate(lines):
            results.append(solve_line(i + 1, line))
            process_results(results)


if __name__ == '__main__':
    main()
