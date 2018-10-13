
# coding: utf-8

# In[3]:

import copy

def returnFirstOutOfOrder(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return i

def replaceWith9s(s, i):
    j = i;
    for j in range(i+1, len(s)):
        s[j] = 9;
    while i >= 0:
        s[i] = s[i] -1;
        i= i-1;
        if s[i] != 9:
            break;
            
    return s;

def solve(s):
    while returnFirstOutOfOrder(s) != None:
        replaceWith9s(s, returnFirstOutOfOrder(s))
    return ''.join([str(z) for z in s if z > 0])


# In[11]:

inputs = """132
1000
7
729
115
810
98
515
616
175
581
421
117
24
171
137
689
73
154
111
508
994
633
3
308
999
706
363
604
138
485
695
523
512
935
435
701
183
444
742
915
346
28
1
757
360
62
543
497
237
837
203
526
881
586
337
951
956
986
193
218
659
651
467
990
878
202
371
910
343
785
369
501
378
562
671
610
430
987
104
831
433
345
983
454
774
125
835
903
181
541
468
525
429
745
637
194
357
976
333""".split('\n')


# In[12]:

for i, p in enumerate(inputs):
    print("Case #"+str(i+1)+": "+str(solve([int(z) for z in list(p)])))


# In[ ]:



