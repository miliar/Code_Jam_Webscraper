#!/usr/bin/env python
"""google code jam : watersheps problem"""


import sys, re


def printM(m):
    for m_row in m :
        print(m_row)
def printFT(m):
    for m_row in m :
        print('['+", ".join(m_row)+']')

def printTM(m):
    def bool2text(v):
        if v :
            return 'T'
        else :
            return 'F'
    for m_row in m :
        print('['+", ".join([bool2text(mV) for mV in m_row])+']')

def analyse_map(map,w,h) :
    sinks = []
    printM(map)
    #flow mask, order if tied: north, west, east, south.
    flowTable = []
    flowKey = ['^','<','>','v','-'] #do not change
    sinks = []
    for j in range(h) :
        flowTable.append([])
        for i in range(w) :
            mv = map[j][i]
            Hdif = [-1, -1, -1, -1] # default no
            if j > 0 : Hdif[0] = mv - map[j-1][i]
            if i > 0 : Hdif[1] = mv - map[j][i-1]
            if i < w-1 : Hdif[2] = mv - map[j][i+1]
            if j < h-1 : Hdif[3] = mv -   map[j+1][i] 
            #print(i,j,Hdif)
            minH = max(Hdif)
            if minH > 0 :
                flowTable[-1].append(flowKey[Hdif.index(minH)])
            else : 
                flowTable[-1].append(flowKey[-1])
                sinks.append([j,i])
    print('flow table')
    printFT(flowTable)

    sinkIDs = [[0 for i in range(w)] for j in range(h)]
    #print('sink IDs blank')
    #printM(sinkIDs )
    def reversePropogateSink(j,i,s_ID):
        #print(j,i,s_ID)
        sinkIDs[j][i]=s_ID
        if j > 0 and flowTable[j-1][i] == 'v' : reversePropogateSink(j-1,i,s_ID)
        if j < h-1 and flowTable[j+1][i] == '^' : reversePropogateSink(j+1,i,s_ID)
        if i > 0 and flowTable[j][i-1] == '>' : reversePropogateSink(j,i-1,s_ID)
        if i < w-1 and flowTable[j][i+1] == '<' : reversePropogateSink(j,i+1,s_ID)
    sID = 1
    for sj,si in sinks :
        reversePropogateSink(sj,si,sID)
        sID = sID + 1
    #print('sink IDs')
    #printM(sinkIDs )
    #now lettering
    basinKeys = {}
    basinTable = []
    for j in range(h) :
        basinTable.append([])
        for i in range(w) :
            sI = sinkIDs[j][i]
            if not basinKeys.has_key(sI):
                basinKeys[sI] = chr(97+len(basinKeys))
            basinTable[-1].append(basinKeys[sI])
    #print('basin table')
    #printFT(basinTable)
    return basinTable

def analyse_datafile(datafile):
    f = file(datafile)
    lines = f.readlines()
    mapN = int(lines[0].strip())
    print('file "%s" contains %i maps' % (datafile,mapN))
    f_ind = 1
    maps = []
    for i in range(mapN) :
        h,w = [ int(v) for v in lines[f_ind].strip().split(' ')]
        alts = []
        for j in range(h) :
            alts.append([ int(v) for v in lines[f_ind+1+j].strip().split(' ')])
        maps.append([h,w,alts])
        f_ind = f_ind + h + 1
    for m in maps :
        print(m)
    output = []
    #h,w,map = maps[0]
    #analyse_map(map,w,h)
    for m,i in zip(maps,range(mapN)) :
        h,w,map = m
        res = analyse_map(map,w,h)
        outText = 'Case #%i:\n' %(i+1)
        outText = outText + '\n'.join([' '.join(row) for row in res])
        print(outText)
        output.append(outText)

    return output


output =  analyse_datafile(sys.argv[1])

fout = file(sys.argv[1]+'_output','w')
fout.write('\n'.join(output))
fout.close()
