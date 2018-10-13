#!/usr/bin/python

"""
Speaking in Tongues problem solution
(GCJ 2012, Qualification Round)
Author: a5kin
"""

import sys

# strings to analize
original = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
            "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
            "de kr kd eoya kw aej tysr re ujdr lkgc jv",
            "y qeez",
            ]
translated = ["our language is impossible to understand",
              "there are twenty six factorial possibilities",
              "so it is okay if you want to just give up",
              "a zooq",
              ]
# building possible mappings
mappings = {}
for i in range(len(original)):
    for j in range(len(original[i])):
        mappings.update({original[i][j]: translated[i][j]})

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: speaking_in_tongues.py <input file>"
    sys.exit(0)

# get number of cases
T = int(in_file.readline())

# begin prosessing cases
for cur_case in range(T):
    # get string
    string_original = in_file.readline().strip()
    string_translated = ""
    for symbol in string_original:
        if mappings.has_key(symbol):
            string_translated += mappings[symbol]
        elif symbol == " ":
            string_translated += " "
        else:
            string_translated += "?"
    print "Case #%d: %s" % (cur_case + 1, string_translated)

# close input file
in_file.close()

    
        
