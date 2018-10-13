import os
import sys
import itertools


def output_format(string_number,test_case):
    output = "Case #%d:" % (test_case+1)
    output += " %s" % str(string_number)
    output +="\n"
    return output


def are_pancakes_flipped_the_same(pancakes):
    flipped = list(set(pancakes))
    #print flipped
    if len(flipped) == 1:
        return flipped[0]
    else:
        return False


def numbers(string):
    l = []
    print string
    for char in string:
        if char == '-':
            l.append(-1)
        else:
            l.append(1)
    return l


def flip(int_pan):
    print "flipping", int_pan
    return [i * -1 for i in int_pan]

def split_pancakes(pancakes, flipper):
    # print pancakes
    i = 0
    flipping = 0
    int_p = numbers(pancakes)
    while i < len(pancakes)-flipper+1:
        if int_p[i] == -1:
            int_p[i:i+flipper] = flip(int_p[i:i+flipper])
            flipping += 1
        i += 1
        print int_p, flipping, i
    if -1 in int_p:
        return "IMPOSSIBLE"
    return flipping


if __name__ == "__main__":
    # f = open("A-small-practice.in",'r')
    f = open("/home/mike/Desktop/codejam/A-large.in", 'r')
    test_cases = int(f.readline())
    out = open("/home/mike/Desktop/codejam/results_A_large.txt", 'w')

    print test_cases
    for i in range(test_cases):
        input = f.readline().strip("\n")
        (pancakes, flipper) = input.split(" ")

        print 'cc', pancakes
        same_flip = are_pancakes_flipped_the_same(pancakes)
        # print same_flip
        if same_flip == '+':
            result = 0
        else:
            result = -1
            result = split_pancakes(pancakes, int(flipper))
        print result, pancakes
        output = output_format(result, i)
        out.write(output)


