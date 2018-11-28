
# coding: utf-8

# In[9]:

#din = r'p2\samp.txt'
din = r'p2\B-small-attempt0.in'
#din = r'p2\A-large.in'
with open(din, 'r') as f:
    inputs = f.readlines()
    
results = []
all_digits = set(map(str, range(10)))

T = int(inputs[0])
l = 1
while l < len(inputs):
    N, R, O, Y, G, B, V = map(int, inputs[l].split())
    l+=1
    
    # small only
    if max(R,Y,B) > N//2:
        results.append('IMPOSSIBLE')
        continue
    
    res = [None for _ in range(N)]
    
    h = sorted([[R, 'R'], [Y, 'Y'], [B, 'B']], reverse=True)
    
    i = 0
    while i < N:
        if h[0][0] > 0:
            res[i] = h[0][1]
            h[0][0] -= 1
        else:
            res[i] = h[1][1]
            h[1][0] -= 1
        i += 2
    i = 1
    while i < N:
        if h[1][0] > 0:
            res[i] = h[1][1]
            h[1][0] -= 1
        else:
            res[i] = h[2][1]
            h[2][0] -= 1
        i += 2
    
    results.append(''.join(res))
    check_res(res)


# In[5]:

def check_res(res):
    N = len(res)
    for i in range(N):
        assert(res[i] != res[(i + 1)%N])


# In[10]:

dout = r'p2\out.txt'

with open(dout, 'w') as f:
    for i, res in enumerate(results):
        f.write("Case #%d: %s\n" % (i+1, str(res)))


# In[ ]:



