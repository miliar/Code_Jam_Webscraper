import numpy as np
import os
INPUT = os.environ.get("INPUT",'q1_input.txt')
input1 = open(INPUT,'r')
output1 = open('A_output.txt', 'w')

def f(l, k):
    counts = 0
    k = int(k)
    S = np.array([0 if i=='+' else -1 for i in l])
    for i, v in enumerate(S):
        if v != 0:
            if i + k <= S.size:
                S[i:i+k] = -(S[i:i+k] + 1)
                counts+=1
            else:
                counts = "IMPOSSIBLE"
                break
    return counts

q = input1.read().split('\n')
for i in range(1,int(q[0])+1):
    con = q[i].split(' ')
    output1.write('Case #%s: %s\n'%(i, f(con[0], con[1])))
    print(con, f(con[0], con[1]))
input1.close()
output1.close()

