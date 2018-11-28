#!/usr/bin/env py3k
"""
A pattern consists of exactly L tokens. Each token is either a single lowercase letter (the scientists are very sure that this is the letter) or a group of unique lowercase letters surrounded by parenthesis ( and ). For example: (ab)d(dc) means the first letter is either a or b, the second letter is definitely d and the last letter is either d or c. Therefore, the pattern (ab)d(dc) can stand for either one of these 4 possibilities: add, adc, bdd, bdc.

Input

The first line of input contains 3 integers, L, D and N separated by a space. D words follow, each of length L. These are the words that are known to exist in the alien language. N test cases then follow, each consisting of a pattern as described above. You may assume that all known words provided are unique.

Output

For each test case, output

Case #X: K
where X is the test case number, starting from 1, and K indicates how many words in the alien language match the pattern.

Limits

Small dataset

1 ? L ? 10
1 ? D ? 25
1 ? N ? 10
Large dataset

1 ? L ? 15
1 ? D ? 5000
1 ? N ? 500
"""
import sys
import re

text = sys.stdin.readlines()
firstline = text.pop(0).strip()
(len, nowords, cases) = firstline.split(' ')

words = []
for w in range(0, int(nowords)):
    words.append(text.pop(0).strip())

patterns = []
for line in text:
    patterns.append(line.strip())

regexes = []
for pattern in patterns:
    regexes.append('^' + pattern.replace('(', '[').replace(')', ']') + '$')

i = 1
for regex in regexes:
    count = 0
    for word in words:
        if re.match(regex, word) is not None:
            count += 1
    print('Case #%s: %s' % (i, count))
    i += 1