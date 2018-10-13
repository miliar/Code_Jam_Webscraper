#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys


for case in xrange(int(sys.stdin.readline())):
    s_number = sys.stdin.readline().strip()
    diglist = [c for c in s_number]
    for suffix_len in xrange(2, len(diglist)+1):
        prefix = diglist[:len(diglist)-suffix_len]
        suffix = diglist[-suffix_len:]
        # первая цифра суффикса меняется, иначе бы мы обошлись меньшим суффиксом
        # меняем её на наименьшую возможную
        available_first = filter(lambda x: x > suffix[0], suffix)
        if not available_first:
            continue
        middle_char = min(available_first)
        suffix.remove(middle_char)
        suffix.sort()
        result = ''.join(prefix) + middle_char + ''.join(suffix)
        break
    else:
        available_first = filter(lambda x: x > '0', diglist)
        middle_char = min(available_first)
        diglist.remove(middle_char)
        diglist.sort()
        result = middle_char + '0' + ''.join(diglist)

    print "Case #%i: %s" % (case+1, result)

# vim:set tabstop=4 softtabstop=4 shiftwidth=4 expandtab: 
