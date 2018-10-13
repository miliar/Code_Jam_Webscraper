'''
Created on 03.09.2009

@author: Vlad Dumitrescu
'''

import re

if __name__ == '__main__':
    s = ""
    exps = []
    
    # open file
    f = open('A-large.in', 'r')
    
    # read parameters (only d is needed later)
    [l, d, n] = str(f.readline()).split(' ')
    
    # read file
    i = 1
    for line in f:
        if (i > int(d)):
            # patterns are after dictionary
            exps.append(str(line))
        else:
            # add to dictionary string
            s += str(line)
        i += 1
    f.close()
    
    # open file for writing
    f = open('A-large.out', 'w')
    
    # look for every pattern in dictionary string
    i = 1
    for e in exps:
        f.write('Case #' + str(i) + ': ')
        # add "|" to make a valid regex
        e = re.sub('([a-z])(?=[^)(]+[)])', r'\1|', e)
        # find all matches and print resulting list's length
        f.write(str(len(re.findall(e, s))) + '\n')
        i += 1
    f.close()
