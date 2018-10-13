import math
import os

f_in = open('D-small-attempt2.in.txt')
f_out = open('output.out', 'w')
d_in = f_in.readlines()
f_in.close()


d_out = []
for i,s in enumerate(d_in[1:]):
    (x,r,c) = map(lambda x: int(x), s.split(" "))
    if (r*c)%x == 0:
        if max(r,c) >= x:
            if min(r,c) > math.ceil(x/2) or x <= 3 and min(r,c) >= x-1:
                d_out.append('Case #' + str(i + 1) +': GABRIEL' + '\n')
            else:
                d_out.append('Case #' + str(i + 1) +': RICHARD' + '\n')
        else:
            d_out.append('Case #' + str(i + 1) +': RICHARD' + '\n')            
    else:
        d_out.append('Case #' + str(i + 1)  + ': RICHARD' + '\n')
f_out.writelines(d_out)
f_out.close()