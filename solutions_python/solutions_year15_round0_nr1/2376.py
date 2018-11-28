#!/usr/bin/python2
# -*- coding: utf-8 -*-

'''
[COPYRIGHT PLACEHOLDER]
'''
__author__ = 'wojciechm'

'''
Problem

It's opening night at the opera, and your friend is the prima donna (the lead female singer).
You will not be in the audience, but you want to make sure she receives a standing ovation
-- with every audience member standing up and clapping their hands for her.

Initially, the entire audience is seated. Everyone in the audience has a shyness level.
An audience member with shyness level Si will wait until at least Si other audience members
have already stood up to clap, and if so, she will immediately stand up and clap.
If Si = 0, then the audience member will always stand up and clap immediately,
regardless of what anyone else does. For example, an audience member with Si = 2 will be seated
 at the beginning, but will stand up to clap later after she sees at least two other people
standing and clapping.

You know the shyness level of everyone in the audience, and you are prepared to invite additional
 friends of the prima donna to be in the audience to ensure that everyone in the crowd stands up
 and claps in the end. Each of these friends may have any shyness value that you wish, not
 necessarily the same. What is the minimum number of friends that you need to invite to guarantee
 a standing ovation?

Input

The first line of the input gives the number of test cases, T. T test cases follow.
Each consists of one line with Smax, the maximum shyness level of the shyest person in the audience,
followed by a string of Smax + 1 single digits. The kth digit of this string (counting starting from 0)
represents how many people in the audience have shyness level k. For example, the string "409" would mean
that there were four audience members with Si = 0 and nine audience members with Si = 2
(and none with Si = 1 or any other value). Note that there will initially always be between 0 and 9
people with each shyness level.

The string will never end in a 0. Note that this implies that there will always be at least one person
in the audience.

Output

For each test case, output one line containing "Case #x: y", where x is the test case number
(starting from 1) and y is the minimum number of friends you must invite.

Limits

1 ≤ T ≤ 100.
Small dataset

0 ≤ Smax ≤ 6.
Large dataset

0 ≤ Smax ≤ 1000.
'''

def input_name_to_output_name(filename):
    return "{}.out".format(filename)

def process_file(input_file):
    output_file = input_name_to_output_name(input_file)
    with open(input_file) as input_handle:
        with open(output_file, "w") as output_handle:
            cases = int(input_handle.readline())
            for case_index in xrange(cases):
                input_line = input_handle.readline()
                max_shyness, people_string = input_line.split(" ", 1)
                friends = 0
                subtract = 0
                people_string = people_string.strip().rstrip("0")
                for shyness_level, num_people_str in enumerate(people_string):
                    additional_friends = max(0, shyness_level - subtract)
                    friends += additional_friends
                    subtract += additional_friends
                    num_people = int(num_people_str)
                    subtract += num_people
                output_handle.write("Case #{}: {}\n".format(case_index + 1, friends))


if __name__ == "__main__":
    process_file("sample.in")
    process_file("A-small-attempt0.in")
    process_file("A-large.in")