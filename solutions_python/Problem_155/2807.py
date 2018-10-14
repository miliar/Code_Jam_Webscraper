# coding: utf8

# Problem

# It's opening night at the opera, and your friend is the prima donna (the lead female singer). You will not be in the audience, but you want to make sure she receives a standing ovation -- with every audience member standing up and clapping their hands for her.

# Initially, the entire audience is seated. Everyone in the audience has a shyness level. An audience member with shyness level Si will wait until at least Si other audience members have already stood up to clap, and if so, she will immediately stand up and clap. If Si = 0, then the audience member will always stand up and clap immediately, regardless of what anyone else does. For example, an audience member with Si = 2 will be seated at the beginning, but will stand up to clap later after she sees at least two other people standing and clapping.

# You know the shyness level of everyone in the audience, and you are prepared to invite additional friends of the prima donna to be in the audience to ensure that everyone in the crowd stands up and claps in the end. Each of these friends may have any shyness value that you wish, not necessarily the same. What is the minimum number of friends that you need to invite to guarantee a standing ovation?
# Input

# The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with Smax, the maximum shyness level of the shyest person in the audience, followed by a string of Smax + 1 single digits. The kth digit of this string (counting starting from 0) represents how many people in the audience have shyness level k. For example, the string "409" would mean that there were four audience members with Si = 0 and nine audience members with Si = 2 (and none with Si = 1 or any other value). Note that there will initially always be between 0 and 9 people with each shyness level.

# The string will never end in a 0. Note that this implies that there will always be at least one person in the audience.

# Output

# For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of friends you must invite.

# Limits
# 1 ≤ T ≤ 100.
# Small dataset
# 0 ≤ Smax ≤ 6.
# Large dataset
# 0 ≤ Smax ≤ 1000.
# Sample

# Input
# 4
# 4 11111
# 1 09
# 5 110011
# 0 1

# Output
# Case #1: 0
# Case #2: 1
# Case #3: 2
# Case #4: 0

import fileinput

def compute_ovation(max_shyness, shyness_dict):
    num_invited = 0
    num_stand = 0
    for key, val in shyness_dict.iteritems():
        if max_shyness <= num_stand:
            break
        if key > num_stand:
            num_invited += key - num_stand
            num_stand += key - num_stand
        num_stand += val
    return num_invited

def main():
    f = fileinput.input()
    count = int(next(f))
    for case in range(1, count+1):
        line = str(next(f))
        parts = line.split()
        max_shyness = int(parts[0])
        shyness_str = parts[1]
        shyness_dict = dict()
        for i in range(max_shyness+1):
            shyness_dict[i] = int(shyness_str[i])
        num_invited = compute_ovation(max_shyness, shyness_dict)
        print ('Case #{}: {}'.format(case, num_invited))

if __name__ == '__main__':
    main()
