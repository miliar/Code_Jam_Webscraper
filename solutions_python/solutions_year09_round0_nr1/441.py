#!/usr/bin/python

import sys
import os

def match(inputs, pattern):
    """inputs: list like ["abc", "bcd"]
       pattern: list like [set("a", "b", "c"), set("x", "y", "z")]
    """
    result_cnt = len(inputs)
    for input in inputs:
        for char, char_set in zip(input, pattern):
            if char in char_set:
                continue
            else:
                result_cnt -= 1
                break
    return result_cnt


def parse_pattern(pattern):
    in_flag = False
    pattern_result = []
    for char in pattern:
        if char == "(":
            pattern_result.append(set())
            in_flag = True
        elif char == ")":
            in_flag = False
        elif in_flag:
            pattern_result[-1].add(char)
        else:
            pattern_result.append(set(char))
    return pattern_result


def main():
    if len(sys.argv[1:]) != 1:
        print "Usage: %s input" % sys.argv[0]
        sys.exit(1)
    fsock = file(sys.argv[1])

    char_cnt, input_cnt, pattern_cnt = \
                [int(value) for value in fsock.readline().split()]

    inputs = [ fsock.readline().strip() for i in range(input_cnt)]
    
    for i in range(pattern_cnt):
        pattern = parse_pattern(fsock.readline().strip())
        print "Case #%s: %s" % (i+1,  match(inputs, pattern))

if __name__ == "__main__":
    main()




