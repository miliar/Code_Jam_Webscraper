import re
from pprint import pprint

fin="water_l.in"
fout="water_l.out"
f=open(fin)
strings=[re.sub("[\r\n]",'',x) for x in f.readlines()]
f.close()

T=int(strings[0])
maps=[]
n=1

    
def fff(rmap,mapx):
    #pprint(rmap)
    changed=False
    for k in xrange(y):
        for j in xrange(x):
            neight={}
            if k<(y-1): #S
                neight[mapx[k+1][j]]=(k+1,j)
            if j<(x-1): #E
                neight[mapx[k][j+1]]=(k,j+1)
            if j>0: #W
                neight[mapx[k][j-1]]=(k,j-1)
            if k>0: #N
                neight[mapx[k-1][j]]=(k-1,j)
            if len(neight.keys()):
                minkey=min(neight.keys())
                miny,minx=neight[minkey]
                if rmap[miny][minx]!='_' and rmap[k][j]=='_':
                    if mapx[miny][minx]<mapx[k][j]:
                        changed=True
                        rmap[k][j]=rmap[miny][minx]                   
                if rmap[miny][minx]=='_' and rmap[k][j]!='_':
                    if mapx[miny][minx]<mapx[k][j]:
                        rmap[miny][minx]=rmap[k][j]
                        changed=True
    return changed

def ffd(rmap,mapx):
    a=fff(rmap,mapx)
    while a:
        #pprint(rmap)
        a=fff(rmap,mapx)
        
f=open(fout,"w")
for i in xrange(T):
    y,x=[int(x) for x in strings[n].split(' ')]
    n+=1
    mapx=[]
    rmap=[]
    val='a'
    for j in xrange(y):
        mapx.append([int(a) for a in strings[n].split(' ')])
        rmap.append(list(x*'_'))
        n+=1
    val='a'
    for c in xrange(y):
        for d in xrange(x):
            if rmap[c][d]=='_':               
                rmap[c][d]=val
                ffd(rmap,mapx)
                val=chr(ord(val)+1)

    f.write('Case #%s:\n' % (i+1))
    for s in rmap:
        f.write(' '.join(s)+'\n')

f.close()
