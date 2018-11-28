
# coding: utf-8

# In[135]:

f = open('B-large.in', 'r')
lines = f.readlines()
f.close()
cases = int(lines[0].rstrip())
filename = open('B-large.out', 'w')


# In[136]:

def solve(val, length):
    arg=[]
    for i in range(length):
        arg.append(int(str(val)[i]))
    mod = 1
    pos = 0
    while mod == 1:
        mod = 0
        for k in range(length-1):
            if arg[k]>arg[k+1]:
                mod = 1
        if arg[pos] > arg [pos+1]:
            for k in range(length - pos -1):
                arg[pos+1+k] = 9
            arg[pos]= arg[pos]-1
            pos = 0
        else:
            pos = pos + 1 
    numstr = ""
    for i in range(length):
            numstr = numstr + str(arg[i])
    out = str(int(numstr))      
    return out


# In[137]:

for i in range(cases):
    length = len(lines[i+1].rstrip())
    val = int(lines[i+1].rstrip())
    if val > 9:
        out = "CASE #" + str(i+1) + ": " + solve(val,length)
    else:
        out = "CASE #" + str(i+1) + ": " + str(val)
    filename.write(out)
    filename.write("\n")


# In[138]:

filename.close()


# In[ ]:



