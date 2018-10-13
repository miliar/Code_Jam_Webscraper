from __future__ import print_function
import os, os.path
directory = 'C:\Users\lucho\Desktop\___tests'
files = os.listdir(directory)
fp = open(os.path.join(directory, files[0]), 'rb')

fp2 = open(os.path.join(directory, '..', 'out1.out'), 'wb')

def make_row(a):
    return map(lambda x: x == '.' and x or int(x), a.strip())

def wp(a, i=None):

    res = filter(lambda x: x != '.', a)
    res = float(sum(res)) / len(res)
    cache_wp[i] = res
    return res

def owp(m, i):

    o = filter(lambda x: x[1] != '.', enumerate(m[i]))
    res=float(sum(map(lambda x: wp(m[x[0]][:i]+m[x[0]][i+1:]), o))) / len(o)
    cache_owp[i] = res
    return res

def oowp(m, i):

    o = filter(lambda x: x[1] != '.', enumerate(m[i]))
    res = float(sum(map(lambda x: owp(m, x[0]), o))) / len(o)
    cache_oowp[i]=res
    return res

lines = fp.readlines()
tests = int(lines[0].strip())
cnt = 1

for l in range(tests):
    cache_wp = {}
    cache_owp = {}
    cache_oowp = {}
    
    n = int(lines[cnt])
    cnt+=1
    m=[]
    for r in range(n):
        m.append(make_row(lines[cnt]))
        cnt+=1
        
    print('Case #%d:' % (l+1), file=fp2)

    for i, x in enumerate(m):
        print(0.25 * wp(x, i) + 0.50 * owp(m, i) + 0.25 * oowp(m, i), file=fp2)

fp.close()
fp2.close()
