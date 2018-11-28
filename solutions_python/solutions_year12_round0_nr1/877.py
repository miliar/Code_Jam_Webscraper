#!/usr/bin/env python

import sys

MAPPING = { 'a': 'y',
            'o': 'e',
            'z': 'q',
            'q': 'z'}

def update_with_hints():
    global MAPPING

    input = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
            "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
            "de kr kd eoya kw aej tysr re ujdr lkgc jv",
    ]

    output = ["our language is impossible to understand",
                "there are twenty six factorial possibilities",
                "so it is okay if you want to just give up",
    ]

    for coded_sentence, english_sentence in zip(input, output):
        for idx, c in enumerate(coded_sentence):
            MAPPING[c] = english_sentence[idx]

    import string
    in_mapping = set(MAPPING.keys())
    missing = set(string.ascii_lowercase) - in_mapping
    tba = set(string.ascii_lowercase) - set(MAPPING.values())
    print tba

def translate(s):
    output = ""
    for c in s:
        output += MAPPING[c]
    return output

if __name__ == "__main__":
    update_with_hints()

    infile = open(sys.argv[1])
    outfile = open('output.txt', 'w')
    no_cases = int(infile.readline())
    for idx, line in enumerate(infile):
        case = idx + 1
        output = translate(line.strip())
        out_str = "Case #%d: %s\n" % (case, output)
        outfile.write(out_str)
        print out_str,

    print MAPPING
