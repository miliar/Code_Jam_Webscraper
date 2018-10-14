import sys
import re #regular expressions, string pattern matching
import math #math stuff
import array #more efficient lists (type constraint)

def solve(release_list, cells, currentbribe):
    if len(release_list) == 0:
        return currentbribe
    release = release_list[0] - 1
    cells[release] = 0
    #moveup
    i = release + 1
    add1 = 0
    #print release
    while i < len(cells):
        if cells[i] == 1:
            add1 +=1
            i += 1
        else:
            break
    #movedown
    i = release - 1
    add2 = 0
    while i >= 0:
        if cells[i] == 1:
            add2 +=1
            i -= 1
        else:
            break
    #print add1, add2
    return solve(release_list[1:],cells, currentbribe + add1 + add2)

#    if headgain > tailgain:
#        #take from head
#        newmin = to_release[0] + 1
#        print (max - min)
#        currentbribe += max - min
#        return solve(to_release[1:], newmin, max, currentbribe)
#    else:
#        newmax = to_release[-1] - 1
#        print (max - min)
#        currentbribe += max - min
#        return solve(to_release[:-1], min, newmax, currentbribe)

def allperms(list):
    if len(list)==1:
        return [list]
    elif len(list)==2:
        return [list,[list[1], list[0]]]
    else:
        result = []
        for i in range(0, len(list)):
            elem = list[i]
            tails = allperms(list[0:i]+list[(i+1):])
            #print tails
            map(lambda t: result.append([elem]+t) ,tails)
        return result

if __name__ == "__main__":
    cases = int(sys.stdin.readline().strip())
    for case in range(1,cases+1):
        print "Case #{0}:".format(case),
        #read and format input here
        pq = map(int,sys.stdin.readline().strip().split())
        p = pq[0]
        q = pq[1]
        to_release = map(int,sys.stdin.readline().strip().split())
        orders = allperms(to_release)
        cells = []
        for c in range(0,p):
            cells.append(1)
        #print cells
        bribe = solve(orders[0],cells, 0)
        for order in range(1,len(orders)):
            cells = []
            for c in range(0,p):
                cells.append(1)
            #print cells
            b = solve(orders[order],cells,0)
            if bribe > b:
                bribe = b
        #print solution
        print bribe;