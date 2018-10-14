# -*- coding: utf-8 -*-
# Google Code Jam 2012 - Qualification Round
# http://code.google.com/codejam/contest/1460488/dashboard#s=p0
# Copyright © 2012 Aluísio Augusto Silva Gonçalves
# This module is free software, licensed under the terms of the Artistic License 2.0


"""
   Speaking in Tongues
"""


import string

import CodeJam


# Find out the mapping
EXAMPLES = [
	('our language is impossible to understand', 'ejp mysljylc kd kxveddknmc re jsicpdrysi'),
	('there are twenty six factorial possibilities', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'),
	('so it is okay if you want to just give up', 'de kr kd eoya kw aej tysr re ujdr lkgc jv'),
]
SOURCE = ''.join(ex[1] for ex in EXAMPLES) + 'qz'
TARGET = ''.join(ex[0] for ex in EXAMPLES) + 'zq'
MAPPING = string.maketrans(SOURCE, TARGET)


@CodeJam.ProblemSolver(__name__, 1)
def solve (input):
	return str(input[0]).translate(MAPPING)
