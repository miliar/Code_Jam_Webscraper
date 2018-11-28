'''
Created on 13-sep-2009

@author: pbruyn0
'''


def processfile(inname,outname):
    infile = open(inname,'r')
    lines = infile.readlines()
    infile.close()
    N = int(lines[0].strip())
    outfile = open(outname,'w')
    currentline = 1
    for cnt in range(1,N+1):
        P,Q = [int(x) for x in lines[currentline].split()]
        currentline +=1
        cells = [int(x) for x in lines[currentline].split()]
        currentline += 1
#        print P,Q
#        print cells
        result = dumbminbribe(P,Q,cells)
        outfile.write('Case #'+str(cnt)+': '+str(result)+'\n')
    outfile.close()
    
def dumbminbribe(P,Q,cells):
    result = 100*100
    for cellorder in all_perms(cells[:]):
        result = min(result, costbribe(P,Q,cells,cellorder))
    return result

def costbribe(P,Q,cellsin,cellorder):
    result = 0
    cells = cellsin[:]
    while len(cellorder)>0:
        allcosts = costallcells(cells,P)
        nextcell = cellorder.pop(0)
        result += allcosts[cells.index(nextcell)]
        cells.remove(nextcell)
    return result
        
    
    
def minbribe(P,Q,cells):
    result = 0
    while len(cells)>=1:
        costs = costallcells(cells,P)
        mincost = min(costs)
        minind = costs.index(mincost)
        result += mincost
        cells[minind:minind+1]=[]
    return result

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]


def costallcells(cells,P):
    if len(cells)==1:
        return [P-1]
    cost = list(range(len(cells)))
    for i,c in enumerate(cells):
        if i==0:
            cost[i]=max(c-1,0)+cells[i+1]-c-1
        elif i==len(cells)-1:
            cost[i] = c-cells[i-1]-1+P-c
        else:
            cost[i] = cells[i+1]-cells[i-1]-2
    return cost
    