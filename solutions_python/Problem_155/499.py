
# coding: utf-8

# In[4]:

from __future__ import print_function


# In[5]:

def friend_min(shy_list):
    friend_count = 0
    stand_count = 0
    max_shy = len(shy_list) - 1
    for i in range(0, len(shy_list)):
        if int(shy_list[i]) == 0:
            continue
        else:
            # check if shy_list[i] will stand
            if stand_count >= i:
                stand_count += int(shy_list[i])
            else:
                diff = i - stand_count
                stand_count = i
                friend_count += diff
                stand_count += int(shy_list[i])
    return friend_count


# In[6]:

case_ind = 0
f_out = open('A-large.out','w')
with open('A-large.in') as f:
    for line in f:
        if case_ind == 0:
            case_ind += 1
            continue
        shy_list = line.strip().split()[1]
        # print ("Case #" + str(case_ind) + ": " + str(friend_min(shy_list)))
        print ("Case #" + str(case_ind) + ": " + str(friend_min(shy_list)), file=f_out)
        case_ind += 1
f_out.close()


# In[ ]:



