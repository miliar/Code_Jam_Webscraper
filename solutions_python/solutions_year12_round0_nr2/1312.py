'''
Created on Apr 14, 2012

@author: yonits
'''

import unittest
from random import randint

EX_NAME = "dancing_with_the_googlers"

EXAMPLES_DICT = {
                 "3 1 5 15 13 11" : "3",
                 "3 0 8 23 22 21" : "2",
                 "2 1 1 8 0" : "1",
                 "6 2 8 29 20 8 18 18 21" : "3"
                 }

def run_test_case(*args):
    N, S, p = args[:3]
    total_points = args[3:]
    
    print "Starting case: N=%d S=%d p=%d, points=%s" % (N, S, p, total_points)
    
    good_for_sure = 0
    good_only_if_surprising = 0
    
    for dancer_points in total_points:
        if dancer_points % 3 == 0:
            if dancer_points / 3 >= p:
                good_for_sure += 1
            elif 0 < dancer_points < 30 and dancer_points / 3 + 1 >= p:
                good_only_if_surprising += 1
        elif dancer_points % 3 == 1 and dancer_points / 3 + 1 >= p:
                good_for_sure += 1
        elif dancer_points % 3 == 2:
            if dancer_points / 3 + 1 >= p:
                good_for_sure += 1
            elif dancer_points < 29 and dancer_points / 3 + 2 >= p:
                good_only_if_surprising += 1
    
    print good_for_sure, good_only_if_surprising
    return good_for_sure + min(S, good_only_if_surprising)

def parse_line(line):
    splitted = line.split()
    result = run_test_case(*[int(x) for x in splitted])
    return result

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
        example_keys = EXAMPLES_DICT.keys()
        input_txt = str(len(EXAMPLES_DICT)) + "\n" + "\n".join(example_keys)
        expected_output = "\n".join(["Case #%d: %s" % (i + 1, EXAMPLES_DICT[key]) for (i, key) in enumerate(example_keys)]) + "\n"

        self.assertEquals(parse_string(input_txt), expected_output)
    
    def test_maximum_lengths_small_data_set_finish_quickly(self):
        for _ in xrange(100):
            num_googlers = randint(1, 3)
            rand_total_points = [str(randint(0, 30)) for _ in xrange(num_googlers)]
            line = " ".join([str(num_googlers), str(randint(0, num_googlers)), str(randint(0, 10))] + rand_total_points)
            print parse_line(line)

    def test_maximum_lengths_large_data_set_finish_quickly(self):
        for _ in xrange(100):
            num_googlers = randint(1, 100)
            rand_total_points = [str(randint(0, 30)) for _ in xrange(num_googlers)]
            line = " ".join([str(num_googlers), str(randint(0, num_googlers)), str(randint(0, 10))] + rand_total_points)
            print parse_line(line)
            
        # I currently test it manually
