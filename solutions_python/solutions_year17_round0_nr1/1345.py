#!/usr/bin/env python2.7
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import Queue

def isAllHappy(list_s):
    for c in list_s:
        if c != '+':
            return False
    return True

def isAllSame(state_s):
    first_c = state_s[0]
    for c in state_s:
        if c != first_c:
            return False
    return True

def isImpossible(state_s, size):
    pancake_len = len(state_s)
    if size <= pancake_len - size:
        return False
    check_list = state_s[(pancake_len-size):size]
    return not isAllSame(check_list)

def flip(s):
    if s == '+':
        return '-'
    return '+'

def flipMostLeft(list_s, size):
    for i in xrange(len(list_s) - size + 1):
        if list_s[i] == '-':
            for j in xrange(i, i + size):
                list_s[j] = flip(list_s[j])
            return list_s
    return 'IMPOSSIBLE'

def flipPanCake(state_s, size):
    if isAllHappy(list(state_s)):
        return 0
    if isImpossible(state_s, size):
        return 'IMPOSSIBLE'
    list_s = list(state_s)
    step = 0
    while 1:
        step += 1
        list_s = flipMostLeft(list_s, size)
        if list_s == 'IMPOSSIBLE':
            return 'IMPOSSIBLE'
        if isAllHappy(list_s):
            return step


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    state_s, size = raw_input().split(' ')
    print "Case #{}: {}".format(i, flipPanCake(state_s, int(size)))
