#!/usr/bin/env python

import sys

FILENAME = sys.argv[1]
OUTPUT = FILENAME[:-2]+"out"
WORDS = []
CASES = []
PATTERNS = []

def store_n_lines_in_list(file, list, n):
    for idx in range(int(n)):
        list.append(file.next().strip())

with open(FILENAME,'r') as input:
    length, num_words, num_cases = input.readline().split()

    store_n_lines_in_list(input, WORDS, num_words)
    store_n_lines_in_list(input, CASES, num_cases)

for case in CASES:
    # (ab)(bc)(ca)
    variant = False
    pattern = []
    variant_group = []
    for char in case:
        if char != '(' and char != ')':
            if variant:
                variant_group.append(char)
                continue
            else:
                pattern.append(char) 
                continue
        if len(variant_group) != 0:        
            pattern.append(''.join(variant_group))
            variant_group = []
        if char == '(':
            variant = True 
        if char == ')':
            variant = False

    PATTERNS.append(pattern)

output_text = ""
for ii in range(len(PATTERNS)): 
    num_words = 0
    for word in WORDS:
        is_valid = True 
        for jj in range(len(word)): 
            if word[jj] not in PATTERNS[ii][jj]:
                is_valid = False
        if is_valid:
            num_words += 1
    output_text = output_text + "Case #%d: %d\n" % (ii+1, num_words)
            
with open(OUTPUT,'w') as output:
    output.write(output_text)
