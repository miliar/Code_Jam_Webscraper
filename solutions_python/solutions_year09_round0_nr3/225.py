#import psyco
from bisect import bisect
text = 'welcome to code jam'
#text = 'weld'
#text = 'welcome'

results_cache = {}

def reset_cache():
    results_cache.clear()
    for letter in xrange(len(text)):
        results_cache[letter] = {}

def build_indexes(line):
    indexes = {}
    
    # eliminate other letters from line. remove if letter in text
 
    for letter in text:
        indexes[letter] = []
    
    for i, letter in enumerate(line):
        if letter in text:
            indexes[letter].append(i)
           
    
    return indexes
            
def count(indexes, letter, constraint):
    if letter == len(text):
        return 1
    result = 0
    all_string_indexes_of_letter = indexes[text[letter]]
    if letter+1 == len(text):
        all_string_indexes_of_next_letter = []
    else:
        all_string_indexes_of_next_letter = indexes[text[letter+1]]
    
    #letters_that_pass_constraint = all_indexes_of_letter[bisect(all_indexes_of_letter, constraint):]
    #for letter_index in letters_that_pass_constraint:
    
    nls = bisect(all_string_indexes_of_letter, constraint)
    
    
    for i in xrange(nls, len(all_string_indexes_of_letter)):
        #if letter + 1 != len(text):
        #    print "Recursing with letter = %s constrained by %d" % (text[letter+1], all_string_indexes_of_letter[i])
        #    pass
        new_nls = bisect(all_string_indexes_of_next_letter, all_string_indexes_of_letter[i])
        if not new_nls in results_cache[letter]:
            results_cache[letter][new_nls] = count(indexes, letter+1, all_string_indexes_of_letter[i])
            #print "Added to cache of letter", letter
        else:
            #print "Got result from cache"
            pass
        
        result += results_cache[letter][new_nls]
    
    return result

def main():
    number_of_cases = int(raw_input())
    for case_number in range(1, number_of_cases+1):
        reset_cache()
        line = raw_input()
        indexes = build_indexes(line)
        #print "Indexes built"
        result = count(indexes, 0, -1)
        print 'Case #%d: %s' % (case_number, "%04d" % (result % 10000))
        
main()

#import random
#for c in xrange(100):
    #reset_cache()
    #line = ''
    #for i in xrange(600):
        #line += random.choice(text)
    
    ##print "Built big line"
    #indexes = build_indexes(line)
    ##print "Indexes built"
    #count(indexes, 0, -1)
    #if c % 10 == 0:
        #print c