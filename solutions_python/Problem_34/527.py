#!/usr/bin/python

"""
  Google Code Jam 2009
  philfifi@free.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100

import psyco
psyco.full()

_debug = 0

def this_word_matches_test_cases(word, test_case_parsed):
    pass

def solve_case(case_no,L, words_l, test_case    ):
    print "-------------- New case", case_no


    all_words_l = [] # Contains list of letters
    for word in words_l:
        tmp_l = []
        for letter in word:
            tmp_l.append(letter)
        all_words_l.append(tmp_l)


    # ---------------
    i = 0
    new_test_case_l = []
    group = []
    inside_paran = False
    for char in test_case:
        if char == '(':
            inside_paran = True
        elif char == ')':
            inside_paran = False
            new_test_case_l.append(group)
            group = []
        else:
            if inside_paran:
                group.append(char)
            else:
                if group:
                    new_test_case_l.append(group)
                    group = []
                else:
                    new_test_case_l.append([char])
    if group:
        new_test_case_l.append(group)


    test_cases_parsed = new_test_case_l

    # ----------
    print test_cases_parsed


    result = 0
    for word in words_l:
        word_matches = True
        for i in range(L):
            if word[i] not in test_cases_parsed[i]:
                word_matches = False
                break


        if word_matches:
            result += 1



    return result


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])

    line  =fd.readline()
    L, D, N = [int(item) for item in line.split()]
    words_l = [None] * D
    for _ in range(D):
        words_l[_] = fd.readline().strip()

    for case_no in range(1, N+1):

        test_case = fd.readline().strip()
        print "test case:", test_case
        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no,
                                                    L, words_l, test_case)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
