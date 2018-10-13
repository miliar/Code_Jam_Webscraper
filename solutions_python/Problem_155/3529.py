import os
with open('a.txt') as f:
    line = f.readlines()

count = len(line)
x = line[0]
x = [int(i) for i in x.split()]


test_cases = x[0];
max_len = []
data = []
ind = []
d = []

for i in range(1, test_cases+1):
    y = line[i]
    data.append(y.strip())

d = [i.split(" ", 1)[1] for i in data]
index = [i.split(" ", 1)[0] for i in data]

for i in range(0, test_cases):
    m = 0
    c = 0
    for j in range(0, int(index[i])+1):
        #print int(d[i][j]), c, j, m
        if int(d[i][j]) !=0:
            if c<j:
                m = m+(j-c)
                c = c+m
            c = c+int(d[i][j])
   
        
    print "Case #{}:".format(i+1), m
         
  

    

