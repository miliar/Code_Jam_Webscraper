#------------------------------------------------------------------------------#
#                       GCJ: Alien Language                                    #
#                     -----------------------                                  # 
#    Author:    Michael Sverdlin                                               #
#    Date:      3/9/09                                                         #
#                                                                              #
#    TODO:                                                                     #
#                                                                              #
#    (c) copyright 2008-2009                                                   #
#------------------------------------------------------------------------------#
#----------------------------------IMPORTS-------------------------------------#

import os
import re
import sys
import time

#----------------------------------GLOBALS-------------------------------------#

#----------------------------------CLASSES-------------------------------------#

#---------------------------------FUNCTIONS------------------------------------#

def create_word(cur, nexts, d):
    con = False
    for i in d:
        if i.startswith(cur):
            con = True
            break
            
    if False == con:
        return 0
    if [] == nexts:
        return 1 if cur in d else 0
    sum = 0
    for i in nexts[0]:
        sum += create_word(cur + i, nexts[1:], d)
    
    return sum
    

def handle_word(word, d, al, word_len):
    parsed = []
    in_paren = False
    cur_paren = []
    for letter in word:
        if (letter not in "()") and (letter not in al):
            return 0
        if "(" == letter:
            in_paren = True
            continue
        
        if ")" == letter:
            in_paren = False
            parsed.append(cur_paren)
            cur_paren = []
            continue
        
        if in_paren:
            cur_paren.append(letter)
            continue
        
        parsed.append([letter])
    
    
    if len(parsed) != word_len:
        return 0
    
    return create_word("", parsed, d)
    
    


def al_lan(txt):
    """
    http://code.google.com/codejam/contest/dashboard?c=90101#
    """
    lines = txt.split("\n")
    
    bounds_line = lines[0]
    bounds = bounds_line.split(" ")
    word_len = int(bounds[0])
    dict_len = int(bounds[1])
    unknown_count = int(bounds[2])
    lines = lines[1:]
    
    word_dict = []
    letters = []
    
    for i in xrange(dict_len):
        word = lines[i].strip()
        word_dict.append(word)
        for letter in word:
            if letter not in letters:
                letters.append(letter)
    
    lines = lines[dict_len:]
    for i in xrange(unknown_count):
        scrambled = lines[i].strip()
        print "Case #%s: %s" % (i + 1, handle_word(scrambled, word_dict, letters, word_len))

#-----------------------------------MAIN---------------------------------------#

def main():
    """
    Entry point... You enter here.
    """
    f = open("al_lan_result.txt", 'w')
    sys.stdout = f
    
    
    text = """3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc"""

    if ((1 < len(sys.argv)) and (os.path.isfile(sys.argv[1]))):
        text = open(sys.argv[1]).read()
    
    al_lan(text)


if "__main__" == __name__:
    try:
        t = time.time()
        main()
        print >> sys.stderr, "That took %s seconds." % (time.time() - t)
        
    except:
        print >> sys.stderr, "The program crashed. Here's why:"
        import traceback
        traceback.print_exc()
    