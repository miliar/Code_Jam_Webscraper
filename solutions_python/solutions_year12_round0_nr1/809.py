"""Speaking in Tongues"""

import sys
import string
from pprint import pprint


english_to_googlerese = {
    ' ': ' ',
    'a': 'y',
    'o': 'e',
    'z':'q'
    }
googlerese_to_english = dict((v, k) for k, v in english_to_googlerese.items())


sample_matchup = [
    ('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
    ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'),
    ('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')]

def build_dict_from_sample(pairs):
    '''Receives pairs of (googlerese, english), returns a translation table.
    dict includes any previous values in (global) googlerese_to_english.
    Assumes both texts have exact same length.
    '''
    d = googlerese_to_english.copy()
    for goo, eng in pairs:
        d.update(zip(goo, eng))
    return d

def missing_letters(table):
    values = set(table.values())

    missing_in_key = [l for l in string.ascii_lowercase if l not in table]
    missing_in_value = [l for l in string.ascii_lowercase if l not in values]
    return missing_in_key, missing_in_value

def translate(s, table):
    return ''.join(table[c] for c in s)

def run(infile):
    table = build_dict_from_sample(sample_matchup)
    missing_key, missing_val = missing_letters(table)
    assert len(missing_key) == len(missing_val) == 1, "Incomplete translation table!"
    table[missing_key[0]] = missing_val[0]
    assert ' ' in table
    # "+1" -> space
    assert len(table) == len(string.ascii_lowercase)+1, "Still incomplete translation table!"

    f = open(infile)
    num = int(f.readline())
    for i in xrange(num):
        line = f.readline().strip()
        print 'Case #{count}: {}'.format(translate(line, table), count=i+1)


if __name__ == '__main__':
    run(sys.argv[1])
