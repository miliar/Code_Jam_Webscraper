import sys
import pdb



with open('test_in.in','r') as f:
	data=f.readlines()

N=int(data[0]);
res="";

for i in range(N):
    #pdb.set_trace()
    ss=[long(_) for _ in data[i+1].split()]
    #print t
    num=0;
    for a in range(ss[0]):
        for b in range(ss[1]):
            if a&b<ss[2]: num+=1
    res_t=str(num)
    res+="Case #"+str(i+1)+": "+res_t +"\n"

#print res

with open('res.txt', 'w') as f:
	f.write(res)
