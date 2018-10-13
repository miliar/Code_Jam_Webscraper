#!/usr/bin/python
# vi: set fileencoding=utf-8 :

'''
Google code jam 2009 qualification round
A: Standing Ovation
'''

def minimum_number_of_friend(S_max, shyness):
    minimum_number = 0
    standing = int(shyness[0])
    for level in range(1, S_max + 1):
        invite = level - standing
        if invite > minimum_number:
            minimum_number = invite
        standing += int(shyness[level])
    return minimum_number


T = int(raw_input())
for case_number in range(1, T + 1):
    S_max, shyness = raw_input().split()
    print 'Case #%d: %d' % (case_number, minimum_number_of_friend(int(S_max), shyness))
