#!/usr/bin/python

import sys

def solve(in_file, out_file, fas_file):
    fas_list = []
    has_content = True
    while has_content:
        fas = fas_file.readline()[:-1]
        if fas != '':
            fas_list.append(int(fas))
        else:
            has_content = False

    cases = int(in_file.readline())
    for case in range(0, cases):
        A, B = [int(x) for x in in_file.readline().split()]
        total = len(filter(lambda x: x>=A and x<=B, fas_list))
        out_file.write("Case #%d: %d\n" % (case+1, total))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print u"Error: Invalid number of arguments. Expected 1 and received %d." % (len(sys.argv) - 1)
        sys.exit(2)

    input_file_name = sys.argv[1]
    output_file_name = input_file_name.split('.')[0] + '.out'
    in_file = open(input_file_name, 'r')
    out_file = open(output_file_name, 'w')
    fair_and_square_file = open('fair_and_square_small.txt', 'r')
    solve(in_file, out_file, fair_and_square_file)
    fair_and_square_file.close()
    in_file.close()
    out_file.close()

