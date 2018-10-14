__author__ = 'cheungkt'

import sys


def main():
    with open(sys.argv[1], 'r') as test:
        f = open("output.txt", 'w')
        for i in range(1, int(test.readline()) + 1):
            string_count = int(test.readline())
            first_string = test.readline()
            second_string = test.readline()

            base_set = []
            for letter in first_string:
                if letter not in base_set or letter != base_set[-1]:
                    base_set.append(letter)

            second_set = []
            for letter in second_string:
                if letter not in second_set or letter != second_set[-1]:
                    second_set.append(letter)

            if base_set == second_set:
                winnable = True
            else:
                winnable = False

            if winnable:
                moves = 0
                first_pos = 0
                second_pos = 0
                first_count = 0
                second_count = 0
                for letter in base_set:
                    while first_pos < len(first_string) and first_string[first_pos] == letter:
                        first_count += 1
                        first_pos += 1
                    while second_pos < len(second_string) and second_string[second_pos] == letter:
                        second_count += 1
                        second_pos += 1
                    moves += abs(first_count - second_count)
                    first_count = 0
                    second_count = 0


                f.write("Case #%i: %i\n" % (i, moves))
                print "Case #%i: %i" % (i, moves)
            else:
                f.write("Case #%i: Fegla Won\n" % i)
                print "Case #%i: Fegla Won" % i


if __name__ == '__main__':
    main()