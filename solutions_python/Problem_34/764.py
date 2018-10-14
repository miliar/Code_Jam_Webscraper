#!/usr/bin/python
from sys import argv
import re

def solve(in_file_name='test.in'):
    in_file = file(in_file_name)
    L, D, N = [int(part) for part in in_file.readline().split(' ')]
    words = []
    for i in xrange(D):
        words.append(in_file.readline().rstrip())
    def get_options_count(fuzzy):
        fuzzy = [f[0] or f[1] for f in re.findall('\((.*?)\)|(.)', fuzzy)]
        words_copy = words[::1]
        for i in xrange(L):
            words_copy = [word for word in words_copy if word[i] in fuzzy[i]]
        return len(words_copy)
    out_file = file(in_file_name.replace('in','out'), 'w')
    i = 0
    for fuzzy in in_file:
        i+=1
        out_file.write('Case #%s: %s\n'%(i, get_options_count(fuzzy.rstrip())))
    out_file.close()
    in_file.close()

if __name__=='__main__':
    solve(argv[1])
