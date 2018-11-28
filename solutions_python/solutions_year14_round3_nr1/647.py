from optparse import OptionParser
import fractions
import math


def solve(fraction):
    if fraction.numerator == 1 and fraction.denominator == 1:
        return 0
    if fraction > 1 or fraction.denominator % 2 == 1:
        return None
    if fraction.numerator == 1:
        two = int(math.log2(fraction.denominator))
        if 2 ** two == fraction.denominator:
            return two
        else:
            return None
    else:
        fraction *= 2
        for i in range(1, math.ceil(fraction.numerator)):
            a = solve(fractions.Fraction(i, fraction.denominator))
            b = solve(fractions.Fraction(fraction.numerator - i, fraction.denominator))
            if a is not None and b is not None and a < 39 and b < 39:
                return 1 + min(a, b)
        return None


def solve_case(input_file):
    p, q = map(int, input_file.readline().split('/'))
    fraction = fractions.Fraction(p, q)
    moves = solve(fraction)
    return moves if moves else 'impossible'


def process_files(input_file, output_file):
    number_of_cases = int(input_file.readline())
    for case in range(number_of_cases):
        result = solve_case(input_file)
        output_file.write('Case #%i: %s\n' % (case + 1, result))


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-i', '--input', dest='inputFile',
                      help='test case file', metavar='FILE')
    parser.add_option('-o', '--output', dest='outputFile',
                      help='result file', metavar='FILE')
    (options, args) = parser.parse_args()

    if not options.inputFile or not options.outputFile:
        parser.error("options -i and -o are not optional")
    else:
        process_files(open(options.inputFile, 'r'), open(options.outputFile, 'w'))