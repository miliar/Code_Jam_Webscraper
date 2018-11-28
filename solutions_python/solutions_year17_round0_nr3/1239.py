
# coding: utf-8

# In[1]:

doc = open("C-sample.in").read()
# doc = open("C-large.in").read()
doc = open("C-small-2-attempt0.in").read()
lines = doc.split("\n")
print(lines)


# In[2]:

def find_ans(n, k):
    ans_max, ans_min = n, k
    
    if(k == 0):
        pass
#         ans_max = int(n / 2)
#         ans_min = int((n - 1) / 2)
#     elif(n / 2 < k):
#         ans_max = 0
#         ans_min = 0
    else:
        tmpK = k - 1
        step = 0

        while True:
            tmpK -= 2**step
            if(tmpK < 0): break
            step += 1
            
#         print('step', step)
        
        s = 0
        for i in range(step):
#             print('i', i)
            s += 2**i
        
#         print('s', s)
        n -= s
        k -= s
        
#         print('tmp', 'n', n, 'k', k)
        maxK = 2**step
#         print('maxK', maxK)
        
        slot = int(n / maxK)
        
#         print('slot', slot)
        
        large_count = n - maxK * slot
        small_count = maxK - large_count
        
#         print('large', large_count, 'small', small_count)
        
        if k <= large_count:
            size = slot + 1
        else:
            size = slot
        
        ans_max = int(size / 2)
        ans_min = int((size - 1) / 2)
        
#         print('size', n)
    
    return ans_max, ans_min


# In[3]:

# ans_max, ans_min = find_ans(1001, 1)
ans_max, ans_min = find_ans(16, 7)

print(ans_max, ans_min)


# In[4]:

T = int(lines[0])

for i in range(1, T+1):
    n, k = lines[i].split(" ")
    n = int(n)
    k = int(k)

    ans_max, ans_min = find_ans(n, k)
    
    print("Case #{0}: {1} {2}".format(i, ans_max, ans_min))


# In[5]:

2**4


# In[6]:

2**0


# In[ ]:



