import math
import os
for f in os.listdir(os.path.dirname(os.path.realpath(__file__))):
    if f.endswith(".in"):
        f_in = open(f)
        f_out = open(f[:-3] + '.out', 'w')
d_in = f_in.readlines()
f_in.close()

d_out = []
for i,s in enumerate(d_in[1:]):
    x = int(s[0])
    r = int(s[2])
    c = int(s[4])
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
