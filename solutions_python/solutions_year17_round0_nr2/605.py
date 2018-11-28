from typing import List


def read_input(path: str) -> List[int]:
    with open(path, 'r') as f:
        f.readline()
        return [int(l) for l in f]


def digit_list(n: int) -> List[int]:
    res: List[int] = []
    while n > 0:
        mod = n % 10
        res.append(mod)
        n = n // 10

    res.reverse()
    return res

def from_digits(digits: List[int]) -> int:
    if not digits:
        return 0
    m = digits[0]
    for n in digits[1:]:
        m *= 10
        m += n

    return m


def biggest_tidy(max_n: int) -> int:
    digits = digit_list(max_n)
    for i in range(0, len(digits) - 1):
        if digits[i+1] >= digits[i]:
            continue

        cutoff = i
        break
    else:
        return max_n

    for i in range(cutoff, -1, -1):
        if i == 0 or digits[i-1] < digits[i]:
            digits[i] -= 1
            for j in range(i+1, len(digits)):
                digits[j] = 9
            break


    return from_digits(digits)


def solve(case: int) -> int:
    return biggest_tidy(case)


def main():
    cases = read_input('B-large.in')
    with open('output.txt', 'w') as out:
        for idx, case in enumerate(cases, start=1):
            solution = solve(case)
            print(f"Case #{idx}: {solution}", file=out)


if __name__ == '__main__':
    main()