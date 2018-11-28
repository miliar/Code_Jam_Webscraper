def int_to_digits(n):
    return [int(char) for char in str(n)]

def solve(n):
    ints = int_to_digits(n)
    prev = -1
    prev_count = 0
    for i in range(len(ints)-1):
        if ints[i] == prev:
            count += 1
        else:
            count = 0
        prev = ints[i]
        if ints[i] > ints[i+1]:
            # fix previous digits same as this digit (if any)
            for k in range(count):
                ints[i-k] = 9
            ints[i-count] = ints[i-count] - 1
            for j in range(i+1, len(ints)):
                ints[j] = 9
            break
    return int(''.join(str(k) for k in ints))

def main():
    case_count = int(input())
    for case_no in range(1, case_count+1):
        n = int(input())
        solution = solve(n)
        print('Case #{0}: {1}'.format(case_no, solution))
if __name__ == '__main__':
    main()
