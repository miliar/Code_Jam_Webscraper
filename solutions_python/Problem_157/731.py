'''
Created on Aug 30, 2009

@author: jirasak
'''

import heapq
import math

mapping = {('j', '1'): 'j', ('k', 'i'): 'j', 
           ('1', 'j'): 'j', ('1', '1'): '1', 
           ('k', 'j'): '-i', ('1', 'k'): 'k', 
           ('k', 'k'): '-1', ('j', 'i'): '-k', 
           ('k', '1'): 'k', ('i', 'j'): 'k', 
           ('1', 'i'): 'i', ('i', 'k'): '-j',
           ('j', 'k'): 'i', ('i', 'i'): '-1', 
           ('i', '1'): 'i', ('j', 'j'): '-1'}

def proc_case(rep, data):
    data = data * rep
    a = data[0]
    minus_cache = 1
    j_begin = 1
    got_i = False
    if a == 'i':
        got_i = True
        pass
    else:
        for b in data[1:]:
            j_begin += 1
            a = mapping[(a, b)]
            if len(a) == 2:
                minus_cache *= -1
                a = a[1]
            if a == 'i':
                got_i = True
                break
    if not got_i:
        return 'NO'
    
    if j_begin >= len(data):
        return 'NO'
    
    got_k = False
    data_k = data[j_begin:]
    b = data[-1]
    j_ends = -1
    if b == 'k':
        got_k = True
    else:
        for a in data_k[:-1][::-1]:
            b = mapping[(a, b)]
            j_ends -= 1
            if len(b) == 2:
                minus_cache *= -1
                b = b[1]
            if b == 'k':
                got_k = True
                break
    if not got_k:
        return 'NO'
    
    
    got_j = False
    data_j = data[j_begin:j_ends]
#     print data_j
    if len(data_j) == 0:
        return 'NO'
    a = data_j[0]
    if len(data_j) == 1 and a == 'j':
        got_j = True
    else:
        for b in data_j[1:]:
            a = mapping[(a, b)]
            j_ends -= 1
            if len(a) == 2:
                minus_cache *= -1
                a = a[1]
    if a == 'j':
        got_j = True
    
    if not got_j:
        return 'NO'
    
    if minus_cache == -1:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
#     mapping = '''1    1    1
# 1    i    i
# 1    j    j
# 1    k    k
# i    1    i
# i    i    -1
# i    j    k
# i    k    -j
# j    1    j
# j    i    -k
# j    j    -1
# j    k    i
# k    1    k
# k    i    j
# k    j    -i
# k    k    -1'''.splitlines()
#     mapping_dict = {}
#     for m in mapping:
#         mapping_dict[(m.split('    ')[0],m.split('    ')[1])] = m.split('    ')[2]
#     print mapping_dict  
    
    afile = file('C-small-attempt4.in')
    aread = afile.readlines()
    afile.close()
    
    aread = [x.strip() for x in aread]
    numcase = int(aread[0])
    
    cline = 1
    for casenum in range(1, numcase + 1):
        aline = aread[cline+1]
        length, rep = [int(x) for x in aread[cline].split(' ')]
        data = aline
        cline += 2
        x = 'Case #%d: %s' % (casenum, proc_case(rep, data))
        print x