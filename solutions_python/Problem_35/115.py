'''
Created on 3-sep-2009

@author: pbruyn0
'''
from numpy import *
import string

def watershed(infilename, outfilename):
    
    infile = open(infilename, 'r')
    lines = infile.readlines()
    infile.close()
    outfile = open(outfilename,'w')
    T = int(lines[0].strip())
    linecnt = 1
    todirection = [(1,0),(0,1),(0,-1),(-1,0)]
    for tcnt in range(T):
        letters = list(string.ascii_lowercase) 
        outfile.write('Case #'+str(tcnt+1)+':\n')
        H,W=[int(x) for x in lines[linecnt].split()]
        linecnt+=1
        map = zeros([H+2,W+2])+inf
        for mcnt in range(H):
            map[mcnt+1,1:-1]=[int(x) for x in lines[linecnt].split()]
            linecnt+=1
#        print map
        frommap = emptylist(H,W)
        sinks=set()
        for hpos in range(1,H+1):
            for wpos in range(1,W+1):
                #N,W,E,S
                vals = array(map[[hpos-1,hpos,hpos,hpos+1], \
                                   [wpos,wpos-1,wpos+1,wpos]])
#                print 'pos:',hpos,wpos
                
                minind = vals.argmin()
#                print vals,minind, todirection[minind]
                if vals[minind]<map[hpos,wpos]: #no sink, add reverse direction
                    frommap[hpos-1-todirection[minind][0]][wpos-1-todirection[minind][1]].append(todirection[minind])
#                    print (hpos-1-todirection[minind][0],wpos-1-todirection[minind][1]),':',todirection[minind]
                else: #sink
                    sinks.add((hpos-1,wpos-1))
#        print frommap
        # Label according to sinks using a number
        labelnum = zeros([H,W])-1
        queue = []
        print sinks
        for si,s in enumerate(sinks):
            labelnum[s]=si
            queue.append(s)
        while len(queue)>0:
            ci = queue.pop()
#            print 'ci', ci
#            print frommap[ci[0]][ci[1]]
            for neighb in [(ci[0]+n[0],ci[1]+n[1]) for n in frommap[ci[0]][ci[1]]]:
#                print neighb
                if not labelnum[neighb] == -1:
                    print 'Ik denk niet dat dit mag gebeuren'
                labelnum[neighb] = labelnum[ci]
                queue.append(neighb)
        print labelnum
        labeldict={}
        for hpos in range(H):
            for wpos in range(W):
                l = labelnum[hpos,wpos]
                if not l in labeldict:
                    labeldict[l] = letters.pop(0)+' '
                outfile.write(labeldict[l])
            outfile.write('\n')
    outfile.close()
                
        

def emptylist(h,w):
    return [[ [] for i in range(w)] for i in range(h) ]
