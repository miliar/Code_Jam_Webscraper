from __future__ import with_statement

import sys
sys.setrecursionlimit(20000)

def process(se, q, switch = 0):
    if len(q) == 0:
        return switch
    rank = {}

    notin = False
    for i in se:
        if q.count(i)>0:
            rank[i] = q.index(i)
        else:
            notin = i

    if notin == False:
        a,b = rank[se[0]],0
        for i in rank:
            if rank[i]>b:
                a = i
                b = rank[i]
        #print a
        switch += 1
        #print b,q
        return process(se,q[b:],switch)     
        
    else:
        return switch

#a = ['Yeehaw','NSM','Dont Ask','B9','Googol']
#b = ['Yeehaw','Yeehaw','Googol','B9','Googol','NSM','B9','NSM','Dont Ask','Googol']

#print process(a,b)


def eatFile(path_in,path_out):
    with file(path_in,'r') as f_in:
        N = int(f_in.readline().replace('\n',''))
        
        with file(path_out, 'w') as f_out:
            for i in xrange(0,N):
                se_n = int(f_in.readline().replace('\n',''))
                se = []
                for j in xrange(0,se_n):
                    entry = f_in.readline().replace('\n', '')
                    se.append(entry)
                q_n = int(f_in.readline().replace('\n',''))
                q = []
                for j in xrange(0,q_n):
                    entry = f_in.readline().replace('\n','')
                    q.append(entry)

                r = process(se,q)
                s = 'Case #%d: %d' % (i+1,r)

                #print '\n\n\n\n'
                #print se,'\n\n'
                #print q,'\n'

                print s
                f_out.write(s+'\n')
            
                
eatFile('A-large.in', 'prova2.txt')


#a = ['A', 'B'] 
#b = ['A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A']
#print process(a,b)












                
