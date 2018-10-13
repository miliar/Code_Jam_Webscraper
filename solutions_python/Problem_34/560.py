#!/usr/bin/env python
'''
Created on 03/09/2009

@author: safarme
'''

import sys;
import re;

words = []
wordSize = 0

def parse(input):
    # split up input string into tokens
    open = False
    string = ""
    
    for char in input:
        if open:
            string += char
            if char == ')':
                open = False
        else:
            if char == '(':
                string += '('
                open = True
            else:
                string += '(%s)' % char
    
    
    regex = '\((.{1,}?)\){1,%(count)d}?' % {'count':wordSize}
    indexes = [re.sub("[^a-z]", "", x.group()) for x in re.finditer(regex, string)]
    
    # create lists of possible matches
    filtered = words[:]
    tmp = []
    
    # loop over each word and filter non-matches
    for off in range(wordSize):
        for word in filtered:
            if off < len(word) and word[off] in indexes[off]:
                tmp.append(word)
        
        filtered = tmp
        tmp = []
    
    return len(filtered)

if __name__ == '__main__':
    name = sys.argv[1]
    file = open(name)
    (l,d,k) = [int(x) for x in file.readline().split(" ")]
    wordSize = l
    
    for i in range(d):
        words.append(file.readline().strip())
            
    results = []
    out = open(name.replace('.in', '.out'), 'w')
    for case in range(k):
        result = parse(file.readline().strip())
        string = 'Case #%d: %s\n' % (case + 1, result)
        out.write(string)
        