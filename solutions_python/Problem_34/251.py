import re

def assemble_regex(pat):
    
    result = ''
    start_group = 0
    pointer = 0
    
    while True:
        start_group = pat.find("(", pointer)
        
        if start_group == -1:
            result += pat[pointer:]
            break
        
        end_group = pat.find(")", start_group)
        letters_to_join = pat[start_group+1:end_group]
        
        regex = '(' + '|'.join(letters_to_join) + ')'
        
        result += pat[pointer:start_group]
        result += regex
        pointer = end_group+1
        
    return result
        

def main():
    length, num_words, number_of_cases = map(int, raw_input().split())

    text = []
    full_text = ''

    for x in xrange(num_words):
        word = raw_input()
        text.append(word)
        
    full_text = '\n'.join(text)

    for case_number in range(1, number_of_cases+1):
        pattern = raw_input()
        regex = assemble_regex(pattern)
        
        result = len(re.findall(regex, full_text))
        
        print 'Case #%d: %d' % (case_number, result)
main()


#import random
#text=  []
#for i in xrange(5000):
    #word = ''
    #for i in xrange(15):
        #word += random.choice('abcdefghijklmno')
        
    #text.append(word)

#full_text = '\n'.join(text)

#print "now matching"
#regex = assemble_regex('(abcdefghijklmno)'*15)
#for i in xrange(500):        
    #result = len(re.findall(regex, full_text))
    
    #print 'Case #%d: %d' % (i, result)