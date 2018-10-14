'''
Created on Apr 14, 2012

@author: yonits
'''

import unittest
from random import choice

EX_NAME = "speaking_in_tongues"

CASE_1_INPUT = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
CASE_1_EXPECTED_OUTPUT = "our language is impossible to understand"
CASE_2_INPUT = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
CASE_2_EXPECTED_OUTPUT = "there are twenty six factorial possibilities"
CASE_3_INPUT = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
CASE_3_EXPECTED_OUTPUT = "so it is okay if you want to just give up"

translate_dict = {"a":"y", "o":"e", "z":"q"}

for i in xrange(len(CASE_1_INPUT)):
    translate_dict[CASE_1_INPUT[i]] = CASE_1_EXPECTED_OUTPUT[i]

for i in xrange(len(CASE_2_INPUT)):
    translate_dict[CASE_2_INPUT[i]] = CASE_2_EXPECTED_OUTPUT[i]

for i in xrange(len(CASE_3_INPUT)):
    translate_dict[CASE_3_INPUT[i]] = CASE_3_EXPECTED_OUTPUT[i]
    
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter not in translate_dict.keys():
        print letter, "is not in keys"
    if letter not in translate_dict.values():
        print letter, "is not in values"

# what i learned is that q -> z
translate_dict["q"] = "z"
    
print "translate len:", len(translate_dict)

def parse_line(line):
    return "".join([translate_dict[x] for x in line])

def parse_string(string):
    lines = string.splitlines()
    num_cases = int(lines[0])

    result = ""
    for case in xrange(num_cases):
        result += "Case #%d: %s\n" % (case + 1, parse_line(lines[1 + case]))
    
    return result

def parse_file(filename):
    return parse_string(open(filename).read())

if __name__ == "__main__":
    file("%s_output.txt" % EX_NAME, "w").write(parse_file("%s.txt" % EX_NAME))
    


class Tests(unittest.TestCase):
    def test_full_given_example(self):
        input = \
"""3
%s
%s
%s
""" % (CASE_1_INPUT,
       CASE_2_INPUT,
       CASE_3_INPUT)

        expected_output = \
"""Case #1: %s
Case #2: %s
Case #3: %s
""" % (CASE_1_EXPECTED_OUTPUT,
       CASE_2_EXPECTED_OUTPUT,
       CASE_3_EXPECTED_OUTPUT)

        self.assertEquals(parse_string(input),
                          expected_output)
    
    def test_line_1(self):
        self.assertEquals(parse_line(CASE_1_INPUT), CASE_1_EXPECTED_OUTPUT)

    def test_line_2(self):
        self.assertEquals(parse_line(CASE_2_INPUT), CASE_2_EXPECTED_OUTPUT)

    def test_line_3(self):
        self.assertEquals(parse_line(CASE_3_INPUT), CASE_3_EXPECTED_OUTPUT)

    def test_maximum_lengths_finish_quickly(self):
        for _ in xrange(30):
            print parse_line("".join([choice(" abcdefghijklmnopqrstuvwxyz") for _ in xrange(100)]))

        # I currently test it manually
