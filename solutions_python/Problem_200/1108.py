
# coding: utf-8

# In[19]:

#din = r'p2\samp.txt'
din = r'p2\B-small-attempt0.in'
#din = r'p2\B-large.in'
with open(din, 'r') as f:
    inputs = f.readlines()
    
results = []
all_digits = set(map(str, range(10)))

for line in inputs[1:]:
    last_dig = 0
    last_inc = 0
    resdigs = []
    line = line.strip()
    for i, dig in enumerate(line):
        dig = int(dig)
        if (i==0 or dig >= last_dig):
            resdigs.append(dig)
            
            if dig > last_dig:
                last_inc = i
        else:
            for j in range(len(line) - i):
                resdigs.append(9)
            resdigs[last_inc] -= 1
            for j in range(last_inc + 1, len(resdigs)):
                resdigs[j] = 9
            break
        last_dig = dig
        
    i = 0
    while resdigs[i]==0:
        i+=1
    results.append(''.join(map(str, resdigs[i:])))


# In[20]:

dout = r'p2\out.txt'

with open(dout, 'w') as f:
    for i, res in enumerate(results):
        f.write("Case #%d: %s\n" % (i+1, str(res)))


# In[ ]:



