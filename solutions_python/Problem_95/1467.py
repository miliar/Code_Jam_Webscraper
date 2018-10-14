import sys

data = \
[
    ('y qee', 'a zoo'),
    ('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
    ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'),
    ('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up'),
]

def find_mapping(inputs):
    mapping = {}
    for inp in inputs:
        googlerese = inp[0]
        english = inp[1]

        for idx in range(len(googlerese)):
            if googlerese[idx] not in mapping:
                mapping[googlerese[idx]] = english[idx]
            else:
                assert mapping[googlerese[idx]] == english[idx]
    return mapping

def get_diff(l1, l2):
    diff = list(set(l1) - set(l2))
    assert len(diff) < 2
    return diff[0] if len(diff) == 1 else []

def complete_mapping(mapping):
    letters = [chr(xx) for xx in range(ord('a'),ord('a')+26)]
    letters.append(' ')

    diff_keys = get_diff(letters, mapping.keys())
    diff_values = get_diff(letters, mapping.values())

    if len(diff_keys) == 1 and len(diff_values) == 1:
        mapping[diff_keys] = diff_values
    return mapping

def translate(mapping, inp_data):
    return ''.join([mapping[xx] for xx in inp_data])

def process_input(mapping, inp):
    lines = inp.readlines()[1:]
    for idx in range(len(lines)):
        print 'Case #%d: %s' % (idx+1, translate(mapping, lines[idx].strip()))

if __name__ == '__main__':
    mapping = find_mapping(data)
    mapping = complete_mapping(mapping)
    process_input(mapping, sys.stdin)
