
# coding: utf-8

# In[3]:

f = open('input', 'r')
g = open('output', 'w')
T = int(f.readline())
for i in range(T):
    N = int(f.readline())
    l = [int(x) for x in list(str(N))]
    borrow = False
    for j in range(len(l) - 1, 0, -1):
        if sorted(l) != l:
            l[j] = 9
            borrow = True if l[j-1] < (l[j-1]-1)%10 else False
            l[j-1] = (l[j-1]-1)%10
        else:
            break
            
    if borrow is True:
        l[0] = l[0] - 1
    num = "".join([str(x) for x in l])
    g.write("Case #{0}: {1}\n".format(i+1, num.lstrip("0")))
    #print("Case #{0}: {1}\n".format(i+1, num.lstrip("0")))

