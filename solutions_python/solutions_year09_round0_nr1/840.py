#!/usr/bin/python

# Python 2.6 solution, GCJ '09 Qualification Round Problem A
# Corey Downing <downing.c@gmail.com>
# Usage: python alien_language.py <input_file>
# Want output to a file? Use redirection, punk.

import sys

def is_valid(test_value, pos, words):
    for word in words:
        if word[:pos] == test_value:
            return True
    return False

def alien_language(line, words, word_length):
    if len(line) < word_length:
        return 0
    word = ''
    choices = 0
    paren = False

    for i in xrange(len(line)):
        c = line[i]
        if c == ')':
            paren = False
        elif c == '(':
            paren = True
        elif paren:
            paren_end_index = i
            while line[paren_end_index] != ')':
                paren_end_index += 1
            new_word = word + c + line[paren_end_index + 1:]
            choices += alien_language(new_word, words, word_length)
        else:
            word += c
            if not is_valid(word, len(word), words):
                return choices

    if word not in words:
        return choices
    else:
        return choices + 1


if __name__ == '__main__':
    with open(sys.argv[1]) as inf:
        case = 1
        words = []

        infoline = inf.readline().split()
        word_length = int(infoline[0])
        num_words = int(infoline[1])
        cases = int(infoline[2])

        for i in range(num_words):
            words += [inf.readline().strip()]

        while case <= cases:
            line = inf.readline().strip()
            print 'Case #%d: %d' % (case, alien_language(line, words, word_length))
            case += 1

