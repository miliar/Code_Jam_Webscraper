
# coding: utf-8

# In[184]:

import math
f = open('C-small-2-attempt0.in', 'r')
lines = f.readlines()
f.close()
cases = int(lines[0].rstrip())
filename = open('C-small-2.out', 'w')


# In[185]:

def solve(stalls, people):
    divi = math.pow(2,math.floor( math.log(people,2))+1)
    ref = int(math.floor(stalls/divi))
    mini=ref
    maxi=ref
    if ( divi * ref + people ) > stalls:
        mini=ref-1
    if (divi * ref - divi/2 + people) > stalls:
        maxi = ref -1
    out = str(maxi)  + " " + str(mini)
    return out


# In[186]:

for i in range(cases):
    nums = lines[i+1].rstrip().split(" ")
    stalls = int(nums[0])
    people = int(nums[1])    
    out = "CASE #" + str(i+1) + ": " + solve(stalls,people)
    filename.write(out)
    filename.write("\n")


# In[187]:

filename.close()


# In[ ]:



