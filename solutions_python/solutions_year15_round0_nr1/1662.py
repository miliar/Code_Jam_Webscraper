#!/usr/bin/env python
'''
Problem

It's opening night at the opera, and your friend is the prima donna (the lead female singer).
ou will not be in the audience, but you want to make sure she receives a standing ovation
- with every audience member standing up and clapping their hands for her.

Initially, the entire audience is seated. Everyone in the audience has a shyness level.
An audience member with shyness level Si will wait until at least Si other audience
members have already stood up to clap, and if so, she will immediately stand up and clap.
If Si = 0, then the audience member will always stand up and clap immediately,
regardless of what anyone else does. For example, an audience member
with Si = 2 will be seated at the beginning, but will stand up to clap later
 after she sees at least two other people standing and clapping.

You know the shyness level of everyone in the audience, and you are prepared
to invite additional friends of the prima donna to be in the audience to ensure
 that everyone in the crowd stands up and claps in the end. Each of these friends
 may have any shyness value that you wish, not necessarily the same. What is the
 minimum number of friends that you need to invite to guarantee a standing ovation?

'''
import sys


def main():
    if len(sys.argv) < 2:
        print  "no filename specified"
        sys.exit(0)
    with open(sys.argv[1], "r") as f:
        t = int(f.readline()) #number of test cases
        for test in range(t):

            _, s_list = f.readline().split()
            people_clapping = 0
            people_missing = 0

            for shyness_level, shy_people in enumerate(map(int, s_list)):
                people_to_add = 0
                if  shyness_level - people_clapping > 0:
                    people_to_add = shyness_level - people_clapping
                people_missing += people_to_add
                people_clapping += shy_people + people_to_add
            print "Case #%d: %d" % (test+1, people_missing)




if __name__ == '__main__':
    main()
