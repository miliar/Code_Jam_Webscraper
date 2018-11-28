#!/usr/bin/env python

import sys

def process_input():
    with open("B-large.in") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def determine_tidy(num):
    old_num = num
    digits = []
    demon = 10
    while num > 0:
        next_d = num % 10
        digits.append(next_d)
        num = num / 10
    # digits = list(reversed(digits))
    counter = 0
    for i in range(0, len(digits) - 1, 1):
        # print old_num, digits[i], digits[i+1]
        if digits[i] < digits[i + 1]:
            return [False, counter, demon]
        counter += 1
        demon *= 10
    return [True, 0, 0]

def determine_max(cur_num, global_counter):
    while cur_num > 0:
        [r, counter, demon] = determine_tidy(cur_num)
        if(r):
            print "Case #" + str(global_counter) + ":", cur_num
            break
        else:
            if (counter - 1) == counter:
                cur_num = (cur_num - 1)
            else:
                cur_num = (cur_num / demon) * demon -1
            # print cur_num

def main():
    content = process_input()
    data_size = int(content.pop(0))
    global_counter = 1
    for line in content:
        cur_num = int(line)
        determine_max(cur_num, global_counter)
        global_counter += 1

main()
