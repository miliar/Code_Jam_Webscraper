INPUT_FILE = __file__.replace('.py', '.input')
OUTPUT_FILE = __file__.replace('.py', '.output')


def solve(n):
    digits = map(int, list(str(n)))
    current = digits[-1]
    for i in xrange(len(digits)-2, -1, -1):
        if digits[i] > max(0, current):
            digits[i+1:] = [9 for _ in digits[i+1:]]
            digits[i] -= 1
        current = digits[i]
    return int(''.join(str(digit) for digit in digits))


def main():

    with open(INPUT_FILE, 'r') as f, open(OUTPUT_FILE, 'w') as g:
        for i, line in enumerate(f):
            if i == 0:

                continue
            n = int(line.strip())
            outline = 'Case #{i}: {soln}\n'.format(i=i, soln=solve(n))
            g.write(outline)
            print outline,


if __name__ == '__main__':
    main()
