
# coding: utf-8

# In[9]:

#din = r'p1\samp.txt'
din = r'p1\A-small-attempt0.in'
#din = r'p1\A-large.in'
with open(din, 'r') as f:
    inputs = f.readlines()
    
results = []
all_digits = set(map(str, range(10)))

for line in inputs[1:]:
    pk, num = line.split()
    pk = [c == '+' for c in pk]
    num = int(num)
    flips = 0
    for i in range(0, len(pk) - num + 1):
        if not pk[i]:
            for k in range(num):
                pk[i+k] = not pk[i+k]
            flips += 1
    if all(pk):
        results.append(flips)
    else:
        results.append('IMPOSSIBLE')


# In[10]:

dout = r'p1\out'

with open(dout, 'w') as f:
    for i, res in enumerate(results):
        f.write("Case #%d: %s\n" % (i+1, str(res)))


# In[ ]:



