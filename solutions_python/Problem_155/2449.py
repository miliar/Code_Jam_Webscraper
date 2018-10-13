
INPUT_PATH = "A-large.in"
OUTPUT_PATH = "A-large.out"


def solve(input):
    result = 0
    smax, digits = input.split(' ')
    smax = int(smax)
    digits = [int(x) for x in digits]
    standing = 0

    for k in xrange(smax + 1):
        digit = digits[k]

        if standing < k:
            result += k - standing
            standing = k

        standing += digit

    return result


def main():
    input_file = open(INPUT_PATH, 'r')
    output_file = open(OUTPUT_PATH, 'w')
    inputs = [x.strip() for x in input_file if len(x)]
    cases = int(inputs.pop(0))

    for i in xrange(cases):
        result = solve(inputs[i])
        output = "Case #%s: %s" % (i + 1, result)
        output_file.write(output + "\n")
        print output

    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
