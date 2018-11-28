#!/usr/bin/python
# -*- coding: utf-8 -*-

import linecache

file_name = './input.txt'
def parse_case_count():
    count = len(open(file_name).readlines())
    return (count - 1) / 10

def main():
    count = parse_case_count()
    for test_count in xrange(count):
        first_answer = linecache.getline(file_name, 1 + test_count * 10 + 1)
        second_answer = linecache.getline(file_name, 1 + test_count * 10 + 6)

        first_row = linecache.getline(file_name, 1 + test_count * 10 + 1 + int(first_answer)).strip()
        second_row = linecache.getline(file_name, 1 + test_count * 10 + 1 + int(second_answer) + 5).strip()
        first_row = set(first_row.split(' '))
        second_row = set(second_row.split(' '))
        intersection =  first_row & second_row

        true_count = int(test_count) + 1
        if len(intersection) == 0:
            print "Case #%s: Volunteer cheated!" % true_count
        elif len(intersection) == 1:
            print "Case #%s: %s" % (true_count, list(intersection)[0])
        elif len(intersection) > 1:
            print "Case #%s: Bad magician!" % true_count

if __name__ == '__main__':
    main()
