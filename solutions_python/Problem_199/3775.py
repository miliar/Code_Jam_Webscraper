import os
import numpy as np

Q = os.environ.get("Q","q.txt")

with open(Q,"r") as rf:
    data = list(map(lambda s:s.strip(),rf.readlines()))
    
n = int(data[0])
qs = data[1:]
assert n == len(qs)

ans_list = []

for q in qs:
    s, k = q.split()
    k = int(k)
    s_dict = {"+":0,"-":1}
    s_array = np.array(list(map(lambda x:s_dict[x],s)))

    ans = 0
    while s_array.sum() > 0:
        i = np.where(s_array==1)[0][0]
        if (len(s_array) - i) >= k:
            s_array[i:(i+k)] = 1 - s_array[i:(i+k)]    
            ans += 1 
        else:
            ans = "IMPOSSIBLE"
            break    
    
    ans_list.append(ans)
    
ans_str = ["CASE #{i}: {a}".format(i=i+1,a=ans_list[i]) for i in range(len(ans_list))]
final_ans = "\n".join(ans_str)

import sys
sys.stdout.write(final_ans)
