#!/usr/bin/python
# Input to stdin, output to stdout. 
# Python 2/3 compatible

import fileinput
input_data = list() 
for line in fileinput.input():
    input_data.append(line)

class SolTestCase: 
    string_one = ""
    string_two = ""
    def __init__(self, s_one, s_two):
        self.string_one = s_one
        self.string_two = s_two
    def output(self, case_num):
        chars_one = ""
        charlen_list_one = list()
        for i in range(0, len(self.string_one)):
            if (len(chars_one) == 0):
                chars_one = self.string_one[i];
                charlen_list_one.append(1)
            else:
                if (self.string_one[i] != chars_one[len(chars_one) - 1]):
                    chars_one += self.string_one[i];
                    charlen_list_one.append(1)
                else:
                    charlen_list_one[len(charlen_list_one) - 1] += 1
        chars_two = ""
        charlen_list_two = list()
        for i in range(0, len(self.string_two)):
            if (len(chars_two) == 0):
                chars_two = self.string_two[i];
                charlen_list_two.append(1)
            else:
                if (self.string_two[i] != chars_two[len(chars_two) - 1]):
                    chars_two += self.string_two[i];
                    charlen_list_two.append(1)
                else:
                    charlen_list_two[len(charlen_list_two) - 1] += 1
        result_str = "ERR"
        if (chars_one != chars_two):
            result_str = "Fegla Won"
        else:
            mutations_reqd = 0
            assert(len(charlen_list_one) == len(charlen_list_one))
            for i in range(0, len(charlen_list_one)):
                mutations_reqd += abs(charlen_list_one[i] - charlen_list_two[i])
            result_str = str(mutations_reqd)

        print ("Case #{0}: {1}".format(case_num, result_str))
               
test_cases = int(input_data[0])
cur_row = 1
for i in range(0, test_cases):
    string_count = int(input_data[cur_row])
    string_one = input_data[cur_row + 1]
    string_two = input_data[cur_row + 2]
    case = SolTestCase(string_one, string_two)
    case.output(i + 1)
    cur_row += (string_count + 1)
    
