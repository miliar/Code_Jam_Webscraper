'''
Created on 14-Apr-2012

@author: abhijit
Statistical Approach
'''
import sys

input_val=int(raw_input())
strings=[]
string_out=[]

map={' ':' ','a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm','z':'q','q':'z'}
for i in range(input_val):
    string=raw_input()
    strings.append(string)

case=1
print 
print
for string in strings:
    output=""
    
    for ch in range(len(string)):
        output+=map[string[ch]]
    string_out.append(output)
    print "Case #"+str(case)+": "+output
    case+=1
    

    

    

    
    

