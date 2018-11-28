'''
Jirasak Chirathivat
'''
import psyco
psyco.full()

import os
import os.path
import sys
sys.setrecursionlimit(1000000000)
#### CHANGE HERE ####
filename = 'c.test'
#### CHANGE HERE ####

def createcell(ncells):
    return [True] * ncells

def breakcell(cells, pos):
    coin = 0
    pos = pos - 1
    #print cells[pos:0:-1], cells, cells[pos+1:]
    for i in reversed(cells[0:pos]):
        if not i:
            break
        coin += 1
    for i in cells[pos+1:]:
        if not i:
            break
        coin += 1
    #print coin
#    print cells#
    cells[pos] = False
#    print cells
    return coin

def permuteOrder(nl):
    result = []
    if len(nl) == 1:
        return [nl]
    for i in range(len(nl)):
        insideList = permuteOrder(nl[0:i] + nl[i+1:])
        for elist in insideList:
            result.append([nl[i]] + elist)
    return result

def findgold(ncells, order):
    cells = createcell(ncells)
    coin = 0
    for pos in order:
        coin += breakcell(cells, pos)
    return coin

def process(casenum, casedata):
    #### CHANGE HERE ####
#    if casenum != 5:
#        return None
    ncells, days, order = casedata
    orders = permuteOrder(order)
    result = []
    #print orders
    for eachorder in orders:
        #print eachorder
        coin = findgold(ncells, eachorder)
        #print coin, eachorder
        result.append(coin)
    return min(result)
    #### CHANGE HERE ####

if __name__ == '__main__':
    afile = file(filename)
    aread = afile.readlines()
    afile.close()
    
    out = file('cout.txt', 'w')
    casefile = file('casefile.txt', 'w')
    
    aread = [x.strip() for x in aread]
    
    numcase = int(aread[0])
    
    line = 1
    
    for i in range(1, numcase + 1):
        
        #### CHANGE HERE ####
        ncells, days = aread[line].split(' ')
        ncells = int(ncells)
        days = int(days)
        
        order = aread[line+1]
        order = [int(x) for x in order.split(' ')]
        #print ncells, days, order
        #### CHANGE HERE ####
        #### CHANGE HERE ####
        #continue
        caseData = (ncells,days, order)
        tomove = 2
        #### CHANGE HERE ####

        if False:
            print >> casefile, 'Case #%s' % i
            print >> casefile, '%s\n' % '\n'.join(aread[line: line + tomove])
            print >> casefile, '%s\n\n\n' % ('\n'.join([str(x) for x in caseData]))
        
        #### CHANGE HERE ####
        line += tomove
        #### CHANGE HERE
        result = process(i, caseData)
        #print 'result', result
        print >> out, 'Case #%s: %s' % (i,  result)
    
    casefile.close()
    out.close()
