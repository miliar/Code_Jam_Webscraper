#!/usr/bin/env python
#
#       QualiA.py
#       
#       Copyright 2009 Unknown <riemy@pcr1>

import re

def decimal_to(number, system):
    rest = list([number % system])
    if number // system != 0:
        rest.extend(decimal_to(number // system, system))
    return rest

def quali_a(correct_words, patterns):
    output = ""
    casenumber = 0
    for pattern in patterns:
        casenumber = casenumber + 1
        possibilities = 0
        pattern = pattern.replace("(","[").replace(")","]")
        pattern_re = re.compile(pattern)
        for word in correct_words:
            if pattern_re.match(word):
                possibilities += 1
        output += "Case #%s: %s\n" % (casenumber, possibilities)
    return output

def main():
    inputfilename = "A-large.in"
    outputfilename = "A-large.out"
    inputfile = open(inputfilename, 'r')
    numbers = inputfile.readline()
    numbers = numbers.split()
    
    wordlength = int(numbers[0])
    number_of_correct_words = int(numbers[1])
    number_of_patterns = int(numbers[2])
    
    correct_words = list()
    patterns = list()
    
    for z in range(number_of_correct_words):
        correct_words.append(inputfile.readline().strip())
    
    for z in range(number_of_patterns):
        patterns.append(inputfile.readline().strip())
        
    inputfile.close()
    
    print correct_words, patterns
    
    output = quali_a(correct_words, patterns)
    print output
    
    outputfile = open(outputfilename,'w')
    outputfile.write(output)
    outputfile.close()
    return 0

if __name__ == '__main__': main()
