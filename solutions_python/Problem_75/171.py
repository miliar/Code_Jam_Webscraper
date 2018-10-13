from __future__ import print_function
import os, os.path
directory = 'C:\Users\lucho\Desktop\___tests'
files = os.listdir(directory)
fp = open(os.path.join(directory, files[0]), 'rb')

fp2 = open(os.path.join(directory, '..', 'out3.out'), 'wb')

lines = fp.readlines()
tests = int(lines[0].strip())

for i in range(tests):
    args = lines[i+1].split()

    c = {}
    for x in args[1:int(args[0])+1]:
        c[x[:2]] = x[2]
        c[x[:2][1] + x[:2][0]] = x[2]
    #print( c)
    
    d = {}
    #print(args[int(args[0])+2:int(args[0])+2+int(args[int(args[0])+1])])
    for p in args[int(args[0])+2:int(args[0])+2+int(args[int(args[0])+1])]:
        d.setdefault(p[0], set()).add(p[1])
        d.setdefault(p[1], set()).add(p[0])
    #print(d)

    ls = set()
    l = []
    prev_in_ls = False
    for x in args[-1]:
        if not l:
            prev_in_ls = False
            l.append(x)
            ls.add(x)
        elif c.get(l[-1] + x):

            if not prev_in_ls:
                ls.remove(l[-1])
            
            comb = c[l[-1] + x]
            l.pop()
            l.append(comb)
            
        elif d.get(x, set()) & ls:
            ls = set()
            l = []
            prev_in_ls = False
        else:
            prev_in_ls = x in ls
            #print(i, x, prev_in_ls)
            l.append(x)
            ls.add(x)
            
    print('Case #%d: %s' % (i+1, str(l).replace('\'', '')), file=fp2)

fp.close()
fp2.close()
