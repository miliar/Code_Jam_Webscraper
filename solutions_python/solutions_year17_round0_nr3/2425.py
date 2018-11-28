
# coding: utf-8

# In[1]:


def get_init_stalls(N):
    return [True] + ([False] * N) + [True]


# In[10]:

def findLR(stall_idx, stalls):
    ii, L = stall_idx - 1, 0
    while not stalls[ii]:
        L += 1
        ii -= 1

    ii, R = stall_idx + 1, 0
    while not stalls[ii]:
        R += 1
        ii += 1

    return L, R


# In[22]:

def pick_next_stall(stalls):
    stall_scores = [(findLR(x, stalls), x)
                    for x in range(len(stalls))
                    if not stalls[x]]
    stall_rule = sorted([(min(scores), max(scores), -num) for scores, num in stall_scores])
    return stall_rule[-1]


# In[23]:

def play_scenario(N, K):
    stalls = get_init_stalls(N)
    choices = []
    for ii in range(K):
        (min_score, max_score, stall_idx) = pick_next_stall(stalls)
        choices.append({
            'max': max_score,
            'min': min_score,
            'idx': -stall_idx
        })
        stalls[-stall_idx] = True

    return choices


T = int(input())

case = 0
while case < T:
    case += 1
    N, K = [int(x) for x in input().split()]
    choices = play_scenario(N, K)
    print('Case #{}: {} {}'.format(case, choices[-1]['max'], choices[-1]['min']))
