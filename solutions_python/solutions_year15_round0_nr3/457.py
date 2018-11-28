
# coding: utf-8

# In[92]:

import sys
import numpy as np


# In[93]:

from __future__ import print_function


# In[94]:

# init dict mul
class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value
mul = Vividict()
mul['1']['1']='1'
mul['1']['i']='i'
mul['1']['j']='j'
mul['1']['k']='k'
mul['i']['1']='i'
mul['i']['i']='-'
mul['i']['j']='k'
mul['i']['k']='J'
mul['j']['1']='j'
mul['j']['i']='K'
mul['j']['j']='-'
mul['j']['k']='i'
mul['k']['1']='k'
mul['k']['i']='j'
mul['k']['j']='I'
mul['k']['k']='-'

mul['-']['1']='-'
mul['-']['i']='I'
mul['-']['j']='J'
mul['-']['k']='K'
mul['I']['1']='I'
mul['I']['i']='1'
mul['I']['j']='K'
mul['I']['k']='j'
mul['J']['1']='J'
mul['J']['i']='k'
mul['J']['j']='1'
mul['J']['k']='I'
mul['K']['1']='K'
mul['K']['i']='J'
mul['K']['j']='i'
mul['K']['k']='1'

mul['1']['-']='-'
mul['1']['I']='I'
mul['1']['J']='J'
mul['1']['K']='K'
mul['i']['-']='I'
mul['i']['I']='1'
mul['i']['J']='K'
mul['i']['K']='j'
mul['j']['-']='J'
mul['j']['I']='k'
mul['j']['J']='1'
mul['j']['K']='I'
mul['k']['-']='K'
mul['k']['I']='J'
mul['k']['J']='i'
mul['k']['K']='1'

mul['-']['-']='1'
mul['-']['I']='i'
mul['-']['J']='j'
mul['-']['K']='k'
mul['I']['-']='i'
mul['I']['I']='-'
mul['I']['J']='k'
mul['I']['K']='J'
mul['J']['-']='j'
mul['J']['I']='K'
mul['J']['J']='-'
mul['J']['K']='i'
mul['K']['-']='k'
mul['K']['I']='j'
mul['K']['J']='I'
mul['K']['K']='-'

# init dict div[x][y]=a, where xa=y
div = Vividict()
for x in ['1', 'i', 'j', 'k', '-', 'I', 'J', 'K']:
    for y in ['1', 'i', 'j', 'k', '-', 'I', 'J', 'K']:
        for key, val in mul[x].items():
            if val == y:
                div[x][y] = key


# In[95]:

def mul_range(s_cumulate_list, start, end):
    return div[(s_cumulate_list[start-1])][(s_cumulate_list[end])]


# In[ ]:

def is_valid(s):
    # calculate s_cumulate
    s_cumulate_list = []
    s_cumulate_list.append(s[0])
    for i in range(1, len(s)):
        s_cumulate_list.append(mul[(s_cumulate_list[-1])][(s[i])])
    s_cumulate_list = np.array(s_cumulate_list)
    s_list = np.array(list(s))
    # calculate s_rev_cumulate_list
    s_rev_cumulate_list = []
    for i in range(0, len(s)):
        s_rev_cumulate_list.append(mul_range(s_cumulate_list, i, len(s)-1))
    s_rev_cumulate_list = np.array(s_rev_cumulate_list)
    # find all i that s[0]*s[1]***s[i] == 'i'
    start_i_index = np.where(s_cumulate_list == 'i')[0]
    # find all k that s[k]*s[k+1]***s[len(s)-1] == 'k'
    end_k_index = np.where(s_rev_cumulate_list == 'k')[0]
    for i in start_i_index:
        for k in end_k_index:
            if i < k:
                if mul_range(s_cumulate_list, i+1, k-1) == 'j':
                    return 'YES'
    return 'NO'


# In[ ]:

in_file = 'C-small-attempt0.in'
out_file = 'c.out'
case_ind = 0
f_out = open(out_file,'w')
with open(in_file) as f:
    # ignore first line
    _ = f.readline()
    # read a case
    while True:
        # read L and X
        line = f.readline()
        if not line: break
        line_list = map(int, line.strip().split())
        L = int(line_list[0])
        X = int(line_list[1])
        if X > 12:
            X = 8 + X % 12
        # read s_unit
        s_unit = f.readline().strip()
        assert(len(s_unit) == L)
        s = s_unit * X
        # print cake_list
        case_ind += 1
        print ("Case #" + str(case_ind) + ": " + is_valid(s), file=f_out)
f_out.close()


# In[ ]:



