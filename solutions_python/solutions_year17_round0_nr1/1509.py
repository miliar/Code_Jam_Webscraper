
# coding: utf-8

# In[39]:

f = open('A-large.in', 'r')
lines = f.readlines()
f.close()
cases = int(lines[0].rstrip())
filename = open('A-large.out', 'w')
pos = 1


# In[40]:

def solve(extract, length, k):
    out = "IMPOSSIBLE"
    arg=[]
    for i in range(length):
        arg.append(extract[i])
    count = 0;
    for i in range(length):
        if i + k < length +1 :
            if arg[i] == "-":
                count = count + 1
                for j in range(k):
                    if arg[i+j] == "+":
                        arg[i+j] = "-"
                    else:
                        arg[i+j] = "+"
    left = 0
    for i in range(length):
        if arg[i]=="-":
             left = -1
    if left == 0:
        out = str(count)
    return out


# In[41]:

for i in range(cases):
    linelength = len(lines[i+1].rstrip())
    for j in range(linelength):
        if lines[i+1][j] == " ":
            length = j
            k = int(lines[i+1][j+1: linelength])
            j = linelength
    out = "CASE #" + str(i+1) + ": " + solve(lines[i+1][0:length],length,k)
    filename.write(out)
    filename.write("\n")


# In[42]:

filename.close()


# In[ ]:



