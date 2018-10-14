#!/usr/bin/env python2.6

# -*- coding : utf-8 -*-


        
        
def roller(R, k, Queue):
        Euros = 0
        for i in range(R):
                count = 1
                while count<len(Queue):
                        if sum(Queue[0:count+1])<=k:
                                count+=1
                        else:
                                break
                Euros += sum(Queue[0:count])
                Queue = Queue[count:] + Queue[0:count]
        return Euros
                

max_R = 1000
max_k = 100
max_N = 10
max_g = 10

per = '\n'
lino = -1
with open("C-small-attempt0.in", "r") as fin:
        with open("C-small.out", "w") as fout:
                for line in fin:
                        lino+=1
                        if lino == 0:
                                T = int(line)*2
                                continue
                        if lino > T:
                                break
                        if lino == T:
                                per = ''
                        if lino % 2:
                                rkn = line.strip().split()
                                R = int(rkn[0].strip())
                                k = int(rkn[1].strip())
                                N = int(rkn[2].strip())
                        else:
                                if not (R>max_R or k>max_k or N>max_N or R<1 or k<1 or N<1):
                                        Queue = line.strip().split()
                                        Queue = map(int, Queue)
                                        for x in Queue:
                                                if x>k or x<1 or x>10:
                                                        fout.write('Case #%d: 0%s' % (lino/2, per))
                                                        continue
                                        Euros = roller(R, k, Queue)
                                        fout.write('Case #%d: %d%s' % (lino/2, Euros, per))
                                else:
                                        fout.write('Case #%d: 0%s' % (lino/2, per))
                                
                                