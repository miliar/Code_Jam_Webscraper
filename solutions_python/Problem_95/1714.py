#!/usr/bin/env python


trans = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', ' ':' '}

def to_english(G):
    return "".join(map(lambda letter: trans[letter], G))
        

if __name__ == '__main__':
    test_cases = int(raw_input())
    for test_case in range(1, test_cases + 1):
        print "Case #%d: %s" % (test_case, to_english(raw_input().strip()))
