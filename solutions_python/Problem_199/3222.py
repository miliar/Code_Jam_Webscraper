
# coding: utf-8

# In[1]:

import copy

def comp_score(s,k):
    
    dst = "+"*len(s)
    
    score_dict = {s:0}
    
    max_score = len(s)-k+1

    for counter in range(max_score):
        counter = max(score_dict.values())
        key_scores = score_dict.items()
        tmp_dict = copy.deepcopy(score_dict)
        for key,score in key_scores:
            if score == counter:
                for i in range(len(key)-k + 1):
                    flipped = flip(key,i,k)
                    if flipped not in tmp_dict:
                        tmp_dict[flipped]=tmp_dict[key]+1

        if dst in tmp_dict:
            return tmp_dict[dst]
        elif counter == max_score-1:
            return "IMPOSSIBLE"
        score_dict = tmp_dict
    


# In[2]:

def flip(s,n,k):
    for i in range(n,n+k):
        if s[i] == '+':
            s = s[:i]+'-'+s[i+1:]
            
        else:
            s = s[:i]+'+'+s[i+1:]
    
    return s


# In[3]:

t = int(input())  # read a line with a single integer

s_list = []
k_list = []

for i in range(1, t + 1):
    s, k = input().split(" ")
    k = int(k)
    # read a list of integers, 2 in this case
    print("Case #{}: {}".format(i, comp_score(s,k)))


# ### k_list

# In[ ]:



