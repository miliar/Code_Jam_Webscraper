from time import *

num_letters = 0
num_words   = 0
test_cases  = 0

words = []
cases = []

def main():    
    line = raw_input()
    
    t = line.split()
    num_letters = int(t[0])
    num_words   = int(t[1])
    test_cases  = int(t[2])
        
    for i in range(num_words):
        line = raw_input()
        words.append( line )

    for i in range( test_cases ):
        line = raw_input()
        cases.append( line )
        
    for i in range( test_cases ):
        result = parse_cases( cases[i], num_letters )
        print 'Case #%d: %d' % (i + 1, result)

def parse_cases( t, letters ):

    roots = []
    possible_words = ['']

    start = False
    len_count = 0
            
    for i in range( letters ):
        roots.append([])
    
    for i in range( len(t) ):
        if t[i] == '(':
            start = True
        elif t[i] == ')':
            start = False
            len_count = len_count + 1
        else:
            roots[len_count].append( t[i] )
            if start == False:
                len_count = len_count + 1
    
    for i in range( len( roots ) ):
        tmp = []
        for j in range( len( roots[i] ) ):
            for k in range( len( possible_words ) ):
                tmp.append( possible_words[k] + roots[i][j] )
        possible_words = check_roots( tmp )
            
    real_count = 0
    for i in range( len( possible_words ) ):
        for j in range( len( words ) ):
            if possible_words[i] == words[j]:
                real_count = real_count + 1
    
    #print possible_words
    
    return real_count

# prune unnecessary roots    
def check_roots( word_list ):
    tmp = []
    for j in range( len( word_list ) ):    
        for i in range( len( words ) ):
            if( words[i].startswith( word_list[j] ) ):
                if not contains( tmp, word_list[j] ):
                    tmp.append( word_list[j] )
    
    return tmp

def contains( l, e):
    for i in range( len( l ) ):
        if l[i] == e:
            return True
    return False
    
def combine_roots( root ):
        
    new_results = []
        
    for i in range( len( possible_words ) ):
        for j in range( len( root ) ):
            new_results.append( results[i] + root[j] )
    
    possible_words = new_results

if __name__ == "__main__":
    main()