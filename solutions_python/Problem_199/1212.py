
# coding: utf-8

# ### a

# In[13]:

# f = open("A-small-attempt0.in", "r").read()
f = open("A-large.in", "r").read()

lines = f.split("\n")
t = int(lines[0])

for no in range(1, t+1):
    line = lines[no]
    columns = line.split(" ")
    str = columns[0]
    n = int(columns[1])

    s = list(str)

    c = 0

    for i in range(0, len(s) - (n - 1)):
#         print(s[i])
        if s[i] == "-":
            c += 1
            for j in range(0, n):
                s[i+j] = "+" if s[i+j] == "-" else "-"
#             print(c, s)
        else:
            pass

#     print(s, c)

    if "-" in s:
        print("Case #{0}: IMPOSSIBLE".format(no))
    else:
        print("Case #{0}: {1}".format(no, c))


# In[ ]:



