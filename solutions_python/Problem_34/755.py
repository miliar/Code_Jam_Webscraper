#!/usr/bin/env python

from __future__ import with_statement
import re

with open('A-large.in', 'r') as f:
    with open('A-large.out', 'w') as o:
        i = 0
        words = []
        length, definition, tests = [int(x) for x in f.readline().split()]
        for line in f:
            result = 0
            line = line.strip()
            i += 1
            if i <= definition:
                words.append(line)
                continue
            else:
                regex = line.replace('(', '[').replace(')', ']')
                regex = re.compile(regex)
                for word in words:
                    if re.match(regex, word):
                        result += 1
            output = "Case #%s: %s\n" % (i-definition, result)
            o.write(output)