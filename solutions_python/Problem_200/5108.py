# -*- coding: utf-8 -*-
"""
Kalifou René TRAORE
"""

import re
from copy import deepcopy
from sys import version_info

def content(fname):
    """
    Reading a file and returning the content (a very long string of chars)
    """
    with open(fname) as f:
        whole = f.read()
    return whole

def process_line(ln,index):
    """
    Processing a line case
    """
    o ="Case #"+str(index+1)+ ": " # Ex:Case #1: 129
    N = ln # Last number counted by Tatiana
    for i in range(int(N),-1,-1):
        if sorted(str(i))==list(str(i)):
            #print "hide: "+str(i) +"\n"
            o += str(i)
            break
    return o  +"\n" #+ " for "+ln+'\n'
    
    
def parse_input(sts):
    """
    -Processing every sentence, line by line
    """
    output = ""#\nProcessing an input : tidy numbers \n\n"
    
    s_n = re.split(r'\n', sts)

    #print "\nInput\n \n"+sts+"\n"
    T = int(s_n[0])    #  Number of cases
    # Test on value of T
    if T > 100 or T < 1:
        return "T out of authorized range"
        
    lines = s_n[1:] # cases
    
    for i in range(T) :
        output += process_line(lines[i],i)
    
    return output


def parse_corpus(fname="./analyzed-corpus_sample.txt" ):
    """
    Parsing a corpus
    """
    cnt = content(fname)
    result = parse_input(cnt)
    print result

#####################################################
############### MAIN #################################
if __name__ == "__main__":
   
    py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2
    fname = "B-small-attempt0.in" #"test_input_tidy_numbers.txt"
    
    while fname == None :
        if py3:
            fname = input("Please enter a filename: ")
        else:   
            fname = raw_input("Please enter a filename: ")
    parse_corpus(fname)