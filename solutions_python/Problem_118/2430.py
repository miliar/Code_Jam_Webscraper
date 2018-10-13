# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:07:02 2013

@author: learningoutcomes
"""
import sys

def palindrome(string):
    rever = ''.join(list(reversed(string)))
    if string == rever:
        return 'palindrome'
    else:
        return 'not a palindrom'
    
def make(ranges):
    ini, final = ranges.split(' ')
    a_dict = {}
    for i in range(1, int(final)+1):
        sqr = i**2
        if sqr >= int(final)+1:
            break
        elif sqr < int(ini):
            continue
        else:
            a_dict[i] =i**2
    #for key in a_dict.keys():
     #   a_dict[key] = key**2
    return a_dict
def find_num(string):
    count = 0
    for key, values in make(string).items():
        if palindrome(str(key)) == 'palindrome' and palindrome(str(values)) == 'palindrome':
            count += 1
    return count

if __name__ == '__main__':
    f = [] 
    try:
        with open(sys.argv[1], 'r') as p:
            for i in p.xreadlines():
                f.append(i.strip('\n'))
    except:
        raise
    out = open('pal_out.txt', 'w')
    for i in range(0, int(f[0])):
        out.write('Case #%d: %d\n' %(i+1, find_num(f[i+1])))
    out.close()
    
    