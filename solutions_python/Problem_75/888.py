'''
Created on 2011-5-7

@author: LJY
'''
import psyco

psyco.full()
fin=file('b.in')
fout=file('b.out','w')

T=int(fin.readline().strip())
for t in range(T):
    trans = {}
    line = fin.readline().strip().split();
    n = int(line[0])
    line = line[1:]
    for i in range(n):
        a = list(line[i])
        r = a[:2]
        key = a[2]
        a = r[:]
        r.reverse()
        a=''.join(a)
        r=''.join(r)
        trans[a] = key
        trans[r] = key
    line = line[n:]
    
    cl = {}
    n = int(line[0])
    line = line[1:]
    for i in range(n):
        a = list(line[i])
        r = a[:2]
        a = r[:]
        r.reverse()
        a=''.join(a)
        r=''.join(r)
        cl[a] = []
        cl[r] = []
    line = line[n:]
    s = line[1]
    rst = []
    for c in list(s):
        rst.append(c)
        #print rst,'=',len(rst)
        while len(rst) > 1:
            a = rst.pop()
            b = rst.pop()
            key = ''.join([a,b])
            #print 'tr=',key
            if key in trans:
                rst.append(trans[key])
            else:
                rst.append(b)
                rst.append(a)
                break;
            
        if len(rst) > 0:
            c = rst[-1]
        for j in range(len(rst) - 1 ):
            a = rst[j]
            key = ''.join([a,c])
            #print 'cl=',key
            if key in cl:
                rst = []
                break        
    print ', '.join(rst)
    fout.write('Case #%d: ['%(t+1))
    fout.write(', '.join(rst))
    fout.write(']\n')
    
                
            
            
fin.close()
fout.close()