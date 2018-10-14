
# coding: utf-8

# In[4]:

#din = r'p1\samp.txt'
din = r'p1\A-small-attempt0.in'
#din = r'p1\A-large.in'
with open(din, 'r') as f:
    inputs = f.readlines()
    
results = []
all_digits = set(map(str, range(10)))

T = int(inputs[0])
l = 1
while l < len(inputs):
    D, N = map(int, inputs[l].split())
    l+=1
    maxt = 0
    for _ in range(N):
        K, S = map(int, inputs[l].split())
        maxt = max(maxt, (D-K)/S)
        l += 1
    
    results.append(D/maxt)


# In[5]:

dout = r'p1\out.txt'

with open(dout, 'w') as f:
    for i, res in enumerate(results):
        f.write("Case #%d: %s\n" % (i+1, str(res)))


# In[ ]:



