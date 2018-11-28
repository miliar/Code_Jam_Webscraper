#!/usr/bin/python

from sys import argv


def main():
    debug = False
    file_in = open(argv[1], 'r')
    test_cases = int(file_in.readline())
    count = 0

    while test_cases:
        count = count + 1
        test_cases = test_cases - 1

        data_line = file_in.readline().rstrip("\n")
        bits = data_line.split()
        my_a = int(bits[0])
        my_b = int(bits[1])

        winner_list = {}
        for my_m in range(my_a, (my_b+1)):
            if my_m < 10:
                break
            digits = list(str(my_m))
            digit_count = len(bits[0])
            for j in range(0, digit_count):
                front = digits[0:j]
                back = digits[j:]
                s_num = str(''.join(back)) + str(''.join(front))
                my_n = int(s_num)
                if my_a <= my_n and my_n < my_m and my_m <= my_b:
                    if debug:
                        print "%s seems to be a winner" % (my_m)
                    hashkey = str(my_n) + "." + str(my_m)
                    winner_list[hashkey] = True
        print "Case #%d: %d" % (count, len(winner_list))

if __name__ == "__main__":
    main()