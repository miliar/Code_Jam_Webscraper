import sys
from copy import copy
 
f = open('/home/moha/pre-releases/code-jam/A-large.in', 'r')
o = open('/home/moha/pre-releases/code-jam/A-large.out', 'w')

(l, d, n) = f.readline().split(' ');

dictionary = {}
_t_dic = {}
_tmp_word = ''
t = 0

for i in range(int(d)):
    _tmp_word = f.readline().strip();
    word = ''
    
    for c in _tmp_word:
        word += c
        _t_dic[word] = True
        
    dictionary[_tmp_word] = True
    
for i in range(int(n)):
    _dict_copy = copy(dictionary)
    
    word = f.readline()
    multi = False 
    pos = 0
    curr = {}
    prev = {'':True}
    
    for c in word:
        if c == '(':
            multi = True
        elif c == ')':
            multi = False
        elif ord(c) >= 97 and ord(c) <= 123:
            for _word in prev:
                if _t_dic.has_key(str(_word) + str(c)):
                    curr[str(_word) + str(c)] = True
        else:
            continue
        
        if multi == False:        
            prev = copy(curr)
            curr = {}
            pos+=1

    wc = 0
    for _word in prev:
        if _dict_copy.has_key(_word) and _dict_copy[_word] == True:
            del _dict_copy[_word]
                
            wc+=1
    
    o.write("Case #" + str(i+1) + ": " + str(wc) + "\n")
    
    _dict_copy = False
            
o.close()
