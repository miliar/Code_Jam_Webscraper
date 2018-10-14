#!/usr/bin/env python

import re

letters_only = re.compile('[ijk1]+')

def read_input(filename):
    words = []
    infile = open(filename)
    inlines = infile.readlines()
    infile.close()
    
    for i in xrange(int(inlines[0])):
        command_line = inlines[2*i+1].rstrip().split()
        X = int(command_line[1])
        letters = inlines[2*i+2].rstrip()
        total_str = ''
        for j in xrange(X):
            total_str += letters
            
        words.append(total_str)
        
    return words
    
def quat(a,b):

    product = None
    if '1' in a:
        if '1' in b:
            product = '1'
        elif 'i' in b:
            product = 'i'
        elif 'j' in b:
            product = 'j'
        elif 'k' in b:
            product = 'k'
    elif 'i' in a:
        if '1' in b:
            product = 'i'
        elif 'i' in b:
            product = '-1'
        elif 'j' in b:
            product = 'k'
        elif 'k' in b:
            product = '-j'
    elif 'j' in a:
        if '1' in b:
            product = 'j'
        elif 'i' in b:
            product = '-k'
        elif 'j' in b:
            product =  '-1'
        elif 'k' in b:
            product = 'i'
    elif 'k' in a:
        if '1' in b:
            product = 'k'
        elif 'i' in b:
            product = 'j'
        elif 'j' in b:
            product = '-i'
        elif 'k' in b:
            product = '-1'
        
    if '-' in a or '-' in b:
        if '-' in a and '-' in b:
            return product
        elif '-' in product:
            return re.search(letters_only,product).group(0)
        else:
            return '-' + product
            
    return product
            
def total_prod(substring):
    q = substring[0]
    if len(substring) == 1:
        return q
    else:
        for char in substring[1:]:
            q = quat(q,char)
        return q   
        
def gives_dijkstra(word):

    i_indices = []
    k_indices = []
    
    # find all subsequences that start at index 0 and reduce to "i"           
    for i in xrange(len(word)-2):
        if i == 0:
            which_letter = word[0]
        else:
            which_letter = quat(which_letter,word[i])
        
        if which_letter == "i":
            i_indices.append(i)
    
    # find all subsequences that end at index -1 and reduce to "k"
    for k in xrange(1,len(word)-1):
        if k == 1:
            which_letter = word[-k:]
        else:
            which_letter = quat(word[-k],which_letter)
        
        if which_letter == "k":
            k_indices.append(k)
            
    # products between k indices
    k_indices = k_indices[::-1]
    k_prods = []
    for i in xrange(len(k_indices)-1):
        subseq = word[-k_indices[i]:-k_indices[i+1]]
        k_prods.append(total_prod(subseq))
        
    n_letters = len(word)    
    
    if len(i_indices) == 0 or len(k_indices) == 0:
        return "NO"
        
    print len(k_prods),len(k_indices)         
    # for all pairs of i and k indices, determine if the subsequence defined
    # by them reduces to 'j'
    for i in i_indices:
        valid_pair = False
        for l,k in enumerate(k_indices):
            if i + k >= n_letters:
                continue
            if not valid_pair:
                j_subseq = word[i+1:-k]
                if len(j_subseq) != 0:
                    which_letter = total_prod(j_subseq)
                    valid_pair = True
                else:
                    pass
            else:
                which_letter = quat(which_letter,k_prods[l-1])
            
            if which_letter == 'j':
                    return "YES"
    
    # did not enter dijkstra                
    return "NO"
    
def main():
    out_stream = open("output_csmall.py",'w')
    cases = read_input("C-small-attempt3.in")
    
    for i,word in enumerate(cases):
        works = gives_dijkstra(word)
        print "Case #%d: %s\n" % (i+1,works)
        out_stream.write("Case #%d: %s\n" % (i+1,works))
        
    out_stream.close()
    print "Done"
    return
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
     
    
    
    
    
    
    
    
    
    
                
