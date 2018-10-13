from __future__ import division
lines = open('inputl.in').read().splitlines()
pos = 0
import math
pi = math.pi
# Don't forget to do pos+1 after using these.
r_i = lambda: int(lines[pos].strip())
r_is = lambda: map(int, lines[pos].strip().split())
r_s = lambda: lines[pos].strip()
r_ss = lambda: lines[pos].strip().split()
r_f = lambda: float(lines[pos].strip())
r_fs = lambda: map(float, lines[pos].strip().split())

test = r_i()
pos+=1
out = open('output2.txt', 'w')

result = 0
for t in range(test):
    n, k = r_is()
    pos+=1
    dims = []
    dims2 = []
    dims3 = []
    for i in range(n):
        r, h = r_is()
        pos+=1
        dims3.append((h*r,r,h))
    dims3.sort(reverse=True)
    for i in range(n):
        dims.append((dims3[i][2], dims3[i][1]))
        dims2.append(dims3[i][0])
    rmax = 0
    st = 0
    result = 0
    for i in range(k-1):
        if dims[i][1]>rmax:
                rmax = dims[i][1]
        st += 2*dims2[i]
    rmax = max(rmax, dims[k-1][1])
    # print rmax
    temp = rmax**2 + 2*dims2[k-1]
    flag = 1
    for i in range(k, n):
        r0 = dims[i][1]
        h0 = dims[i][0]
        new = r0**2 + 2*r0*h0
        if r0>rmax and new>temp:
            flag = 0
            temp = new
            rmax = r0
    st+=temp
    result = pi*st


    # if k!=1:
    #     dims.sort(reverse=True)
    #     sts = []
    #     for i in range(k):
    #         if dims[i][1]>rmax:
    #             rmax = dims[i][1]
    #         temp = dims[i][0]*dims[i][1]
    #         if temp<minval:
    #             minpos= i
    #         sts.append(temp)
    #         st+= temp
    #     result = pi*(rmax**2 + 2* st)
    #     for i in range(k, n):
    #         new = result - minval + dims[i][0]*dims[i][1]
    # else:
    #     result = 0
    #     for i in range(n):
    #         r0 = dims[i][1]
    #         h0 = dims[i][0]
    #         result = max(result, pi*(r0**2 + 2*r0*h0))


    # Result contains answer
    temp = "Case #%d: %0.9f" % (t+1, result)
    print temp
    out.write(temp+'\n')

out.close()
