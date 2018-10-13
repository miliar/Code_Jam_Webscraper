
# coding: utf-8

# In[85]:

doc = open("c-sample.txt").read()
doc = open("B-large.in").read()
lines = doc.split("\n")
print(lines)


# In[86]:

def is_asc(n):
    s = list(n)
    
    for i in range(1, len(s)):
        if(s[i - 1] > s[i]): return False
    return True


# In[87]:

def find_ans(n):
    s = list(n)

    for i in range(1, len(s)):
        if(s[i - 1] > s[i]):
            s[i - 1] = str(int(s[i - 1]) - 1)
            s[i:] = ["9"] * (len(s) - i)
            
#         print(i, s[i - 1])
#         print(i, s[i])
        
    n = "".join(s)
    
    if is_asc(n):
        return str(int(n))
    else:
        return str(int(find_ans(n)))


# In[88]:

# print(find_ans("1110"))
find_ans("111111111111111110")
find_ans("987654321")
find_ans("1230123")


# In[89]:

T = int(lines[0])

for i in range(1, T+1):
    n = lines[i]
    ans = find_ans(n)
    print("Case #{0}: {1}".format(i, ans))


# In[ ]:



