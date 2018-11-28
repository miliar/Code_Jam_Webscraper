#!/usr/bin/python

import sys

t_map = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v',
'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g',
'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w',
'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'z': 'q', ' ': ' '}


def map_from_strings(s1, s2):
    trans_map = {}
    for i in range(len(s1)):
        char1 = s1[i]
        char2 = s2[i]
        if char1 == ' ':
            assert(char2 == ' ')
        else:
            if char1 in trans_map:
                assert(trans_map[char1] == char2)
            else:
                trans_map[char1] = char2

    return trans_map


def print_map(trans_map):
    for char1 in sorted(trans_map.keys()):
        print char1, trans_map[char1]


def determine_map():
    s1 = ''
    s2 = ''

    while True:
        line = sys.stdin.readline()
        if len(line.strip()) == 0:
            break
        s1 += line.strip()

    while True:
        line = sys.stdin.readline()
        if len(line.strip()) == 0:
            break
        s2 += line.strip()

    return map_from_strings(s1, s2)


def translate(inp):
    out = ''
    for char1 in inp:
        out += t_map[char1]
    return out


def translate_init():
    num_cases = int(sys.stdin.readline().strip())
    for i in range(1, num_cases + 1):
        inp = sys.stdin.readline().strip()
        out = translate(inp)
        print 'Case #{0}: {1}'.format(i, out)


translate_init()
