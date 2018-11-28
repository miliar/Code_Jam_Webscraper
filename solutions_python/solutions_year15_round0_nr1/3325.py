
# coding: utf-8

# In[1]:

from __future__ import division
import numpy as np


# In[27]:

#data_file = 'sample.txt'
data_file = 'A-large.in'
output_file = 'A-large.out'


# In[28]:

with open(data_file) as fin, open(output_file, 'w') as fout:
    T = int(fin.readline().strip())
    for i, row in enumerate(fin, 1):
        S_max, S_str = row.strip().split(' ')
        S_max = int(S_max)
        
        friends_to_invite = 0
        n_standing_people = int(S_str[0])
        #print('\nSi, People, Standing, Friends')
        #print('{}\t{}\t{}\t{}'.format(0, int(S_str[0]), n_standing_people, friends_to_invite))
        for Si in range(1, S_max + 1):
            n_Si = int(S_str[Si])
            if n_Si > 0:
                if n_standing_people >= Si:
                    n_standing_people += n_Si
                else:
                    friends_to_invite += (Si - n_standing_people)
                    n_standing_people += (n_Si + Si - n_standing_people)
                    
            #print('{}\t{}\t{}\t{}'.format(Si, n_Si, n_standing_people, friends_to_invite))
                
        fout.write('Case #{}: {}\n'.format(i, friends_to_invite))


# In[ ]:



