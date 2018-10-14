#! /usr/bin/python
# Martin Pool
# https://code.google.com/codejam/contest/1460488/dashboard

from sys import stdin

# Sample data, plus the extra information that z -> q, and 
# by elimination that the reverse is true.
googlish = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
qz
"""

english = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
zq
"""

def remove_space(s):
    return s.replace(" ", "").replace("\n", "")

googlish_chars = remove_space(googlish)
english_chars = remove_space(english)

assert len(googlish_chars) == len(english_chars)

google_to_english = {}
for gc, ec in zip(googlish_chars, english_chars):
    if gc in google_to_english:
        assert google_to_english[gc] == ec
    else:
        google_to_english[gc] = ec

# for gc, ec in sorted(google_to_english.items()): print gc, ec

# now we should know every character
assert len(google_to_english) == 26, len(google_to_english)

def decrypt_string(gs):
    result = []
    for gc in gs:
        result.append(google_to_english.get(gc, gc))
    return ''.join(result)

# cross-check
assert decrypt_string(googlish) == english

# now read input
num_cases = int(stdin.readline())
for i in range(num_cases):
    print 'Case #%d: %s' % (
        i+1, decrypt_string(stdin.readline().rstrip('\n')))
