

# Priority dictionary using binary heaps
# David Eppstein, UC Irvine, 8 Mar 2002
# from: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228

#from __future__ import generators

class priorityDictionary(dict):
    def __init__(self):
        '''Initialize priorityDictionary by creating binary heap
of pairs (value,key).  Note that changing or removing a dict entry will
not remove the old pair from the heap until it is found by smallest() or
until the heap is rebuilt.'''
        self.__heap = []
        dict.__init__(self)

    def smallest(self):
        '''Find smallest item after removing deleted items from heap.'''
        if len(self) == 0:
            raise IndexError, "smallest of empty priorityDictionary"
        heap = self.__heap
        while heap[0][1] not in self or self[heap[0][1]] != heap[0][0]:
            lastItem = heap.pop()
            insertionPoint = 0
            while 1:
                smallChild = 2*insertionPoint+1
                if smallChild+1 < len(heap) and \
                        heap[smallChild] > heap[smallChild+1]:
                    smallChild += 1
                if smallChild >= len(heap) or lastItem <= heap[smallChild]:
                    heap[insertionPoint] = lastItem
                    break
                heap[insertionPoint] = heap[smallChild]
                insertionPoint = smallChild
        return heap[0][1]
    
    def __iter__(self):
        '''Create destructive sorted iterator of priorityDictionary.'''
        def iterfn():
            while len(self) > 0:
                x = self.smallest()
                yield x
                del self[x]
        return iterfn()
    
    def __setitem__(self,key,val):
        '''Change value stored in dictionary and add corresponding
pair to heap.  Rebuilds the heap if the number of deleted items grows
too large, to avoid memory leakage.'''
        dict.__setitem__(self,key,val)
        heap = self.__heap
        if len(heap) > 2 * len(self):
            self.__heap = [(v,k) for k,v in self.iteritems()]
            self.__heap.sort()  # builtin sort likely faster than O(n) heapify
        else:
            newPair = (val,key)
            insertionPoint = len(heap)
            heap.append(None)
            while insertionPoint > 0 and \
                    newPair < heap[(insertionPoint-1)//2]:
                heap[insertionPoint] = heap[(insertionPoint-1)//2]
                insertionPoint = (insertionPoint-1)//2
            heap[insertionPoint] = newPair
    
    def setdefault(self,key,val):
        '''Reimplement setdefault to call our customized __setitem__.'''
        if key not in self:
            self[key] = val
        return self[key]







# Dijkstra's algorithm for shortest paths
# David Eppstein, UC Irvine, 4 April 2002
# from: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/119466

# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228
#from priodict import priorityDictionary

def Dijkstra(G,start,end=None):
    """
    Find shortest paths from the start vertex to all
    vertices nearer than or equal to the end.

    The input graph G is assumed to have the following
    representation: A vertex can be any object that can
    be used as an index into a dictionary.  G is a
    dictionary, indexed by vertices.  For any vertex v,
    G[v] is itself a dictionary, indexed by the neighbors
    of v.  For any edge v->w, G[v][w] is the length of
    the edge.  This is related to the representation in
    <http://www.python.org/doc/essays/graphs.html>
    where Guido van Rossum suggests representing graphs
    as dictionaries mapping vertices to lists of neighbors,
    however dictionaries of edges have many advantages
    over lists: they can store extra information (here,
    the lengths), they support fast existence tests,
    and they allow easy modification of the graph by edge
    insertion and removal.  Such modifications are not
    needed here but are important in other graph algorithms.
    Since dictionaries obey iterator protocol, a graph
    represented as described here could be handed without
    modification to an algorithm using Guido's representation.

    Of course, G and G[v] need not be Python dict objects;
    they can be any other object that obeys dict protocol,
    for instance a wrapper in which vertices are URLs
    and a call to G[v] loads the web page and finds its links.
    
    The output is a pair (D,P) where D[v] is the distance
    from start to v and P[v] is the predecessor of v along
    the shortest path from s to v.
    
    Dijkstra's algorithm is only guaranteed to work correctly
    when all edge lengths are positive. This code does not
    verify this property for all edges (only the edges seen
     before the end vertex is reached), but will correctly
    compute shortest paths even for some graphs with negative
    edges, and will raise an exception if it discovers that
    a negative edge has caused it to make a mistake.
    """

    D = {}    # dictionary of final distances
    P = {}    # dictionary of predecessors
    Q = priorityDictionary()   # est.dist. of non-final vert.
    Q[start] = 0
    
    for v in Q:
        D[v] = Q[v]
        if v == end: break
        
        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                    raise ValueError, \
  "Dijkstra: found better path to already-final vertex"
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v
    
    return (D,P)
            
def shortestPath(G,start,end):
    """
    Find a single shortest path from the given start vertex
    to the given end vertex.
    The input has the same conventions as Dijkstra().
    The output is a list of the vertices in order along
    the shortest path.
    """

    D,P = Dijkstra(G,start,end)
    Path = []
    while 1:
        Path.append(end)
        if end == start: break
        end = P[end]
    Path.reverse()
    return Path


# graph input example
#
#G = { 's' : {'u':10, 'x':5},   # <node> : <dict_of_connected_nodes={<node>:<weight>,<node>:<weight>,...}>,...
#      'u' : {'v':1, 'x':2},
#      'v' : {'y':4},
#      'x' : {'u':3, 'v':9, 'y':2},
#      'y' : {'s':7, 'v':6} \
#    }


#################################################################################
#################################################################################
## 
#################################################################################
#################################################################################




import sys, copy, math,time
sys.setrecursionlimit(10000)

import psyco
#psyco.full()
#psyco.profile()

def assertEquals(res,expect): assert res==expect, res




def make_idgen():
    id = 0
    while True: 
        id += 1 
        yield id
idgen = make_idgen()    

def AS(ds):
    if ds=='a':
        return 'b'
    else:
        return 'a'

def calc(tt,aTimes,bTimes):
    aTimes = [(t1,t2,'a') for t1,t2 in aTimes]
    bTimes = [(t1,t2,'b') for t1,t2 in bTimes]
    
    allTimes = sorted(aTimes+bTimes) # sorted by departure time
    
    trains = [] # ('a'/'b', availTime)
    
    acnt,bcnt = 0,0
    
    for dt,at,ds in allTimes:
        now = dt
        
        resent = False
        for ti in xrange(len(trains)):
            ts,tat = trains[ti]
            if ds==ts and now >= tat:
                trains[ti] = (AS(ds),at+tt) # re-send train
                resent = True
                break
        
        if not resent: # couldn't send old train, send new one
            trains.append((AS(ds),at+tt)) # set train avail later at arrival station (AS)
            if ds=='a': acnt += 1
            else: bcnt += 1
        
    return acnt,bcnt


assert calc(5,[],[]) == (0,0)


## gauge big set performance
#import random
#while True:
#    tt = random.randint(0,60)
#    tmax = 24*60
#    rnd = lambda a: random.randint(0,a)
#    aTimes = [(rnd(tmax),rnd(tmax)) for i in xrange(rnd(100))]
#    bTimes = [(rnd(tmax),rnd(tmax)) for i in xrange(rnd(100))]
#    print tt, len(aTimes), len(bTimes), calc(tt, aTimes, bTimes)


#################################################################################
#################################################################################
## 
#################################################################################
#################################################################################


import os, datetime, re, traceback, time, sys

historyDir = './history'
compareEnabled = False

def performCompare(file1, file2): # user specific comparison
    import commands
    commands.getoutput('kompare -c ' +file1 +' ' +file2)



def _contentEquals(outputStr, fileName):
    fcont = open(fileName, 'r').read()
    return outputStr == fcont

def _printSideBySide(outputStr, fileName):
    flines = open(fileName).read().split('\n')
    outLines = outputStr.split('\n')
    def lfield(lines):
        sMaxw = str(max([len(s) for s in lines]) + 5)
        return '%-' + sMaxw + 's' # like '%-30s'
    fieldl,fieldr = lfield(outLines),lfield(flines)
    for l,r in zip(outLines, flines):
        d = {True: 'DIFFERS', False: ''}[l != r]
        print (fieldl +' ' +fieldr + ' %s') % (l,r,d)

_output  = None
_caseNum = None

def rmre(path, patternStr, recursive=False):  # remove files matched by regex pattern 
    pattern = re.compile(patternStr)
    for fname in os.listdir(path):
        if pattern.search(fname):
            name = os.path.join(path, fname)
            try: 
                os.remove(name)
            except:
                if recursive:
                    rmre(name, '')
                    os.rmdir(name)

def outputCase(case):
    global _output,_caseNum
    if type(case) in (list,set,tuple): # line(s) separately?
        for i in range(len(case)):
            line = case[i]
            if i == 0:
                _output += "Case #%d: %s\n" % (_caseNum, str(line))
            else:
                _output += str(line)
    elif type(case) in (str,int,float):
        _output += "Case #%d: %s\n" % (_caseNum, str(case))
    _caseNum += 1

def run(probId, linesFunc, skipFirstLine=True): # linesFunc(inputLines), probId: "A" or "B" etc 
    global _output,_caseNum
    
    for setName in ('sample', 'small', 'large'):
        inFile  = probId + '-' + setName + '.in'
        outFile = probId + '-' + setName + '.out'
        
        if not os.path.exists(inFile):
            print 'INPUT MISSING:', inFile
            continue

        # clear previous output
        _output = ""
        _caseNum = 1

        # execute solver
        try:
            inputlines = open(inFile).readlines()
            inputlines = [l.strip('\n') for l in inputlines] # remove leading newlines
            if skipFirstLine:
                inputlines = inputlines[1:]
            startTime = time.time()
            linesFunc(inputlines)
            duration = time.time() -startTime
        except:
            traceback.print_exc()
            print 'ERRORS WHILE RUNNING:', inFile
            print _output
            print 'ERRORS WHILE RUNNING:', inFile
        
        # remove excess '\n' from end of output
        _output = _output.strip('\n')
        
        # save trial output, correctness unknown
        fnBody = probId + '-' + setName + '.try_'
        ts = datetime.datetime.now().strftime('%j%H_%M%S')
        tryFile = fnBody +ts
        try: os.makedirs(historyDir)
        except: pass
        tryFileHist = os.path.join(historyDir, tryFile)
        rmre('./', '^' + fnBody + r'\d{5}_\d{4}$')
        open(tryFile, 'w').write(_output)
        open(tryFileHist, 'w').write(_output)

        # check output validity if reference avail
        if os.path.exists(outFile):
            if _contentEquals(_output, outFile):
                print 'PASSED (%.3f secs): %s' % (duration,setName)
                os.remove(tryFile) # no need to keep dupes with the .out
                os.remove(tryFileHist)
            else:
                print 'FAILED:', setName
                _printSideBySide(_output, outFile)
                print 'FAILED:', setName
                try:
                    if compareEnabled:
                        print 'Comparing...'
                        performCompare(outFile, tryFile)
                except:
                    print 'Problem running comparison, skipped.'
                return
        else:
            if setName == 'sample':
                print 'SAMPLE OUTPUT MISSING! (%s)' % (outFile,)
            else:
                print 'READY FOR SUBMIT (%.3f secs): %s\n%s' % (duration,setName,os.path.abspath(tryFile))
    print '\nprogram file:'
    print os.path.abspath(sys.argv[0])

def parseLine(line, *types):
    parts = line.split()
    if len(types) == 0:
        if len(parts) == 1:
            return parts[0]
        elif len(parts) == 0:
            return None
        else:
            return parts
    else:
        # cast to given types and
        # repeat from beginning if less types
        casts = []
        for pi in xrange(len(parts)):
            ti = pi % len(types)
            casts.append(types[ti](parts[pi]))
        if len(casts) == 1:
            return casts[0]
        elif len(casts) == 0:
            return None
        else:
            return casts

assert parseLine('1 2 3',int) == [1,2,3]
assert parseLine('1 2 3',str,str,int) == ['1','2',3]
assert parseLine('1 2 3') == ['1','2','3']
assert parseLine('1 s 5.5', int,str,float) == [1, 's', 5.5]
assert parseLine('1', int) == 1
assert parseLine('test test2') == ['test', 'test2']
assert parseLine('test test2', str) == ['test', 'test2']
assert parseLine('test') == 'test'
assert parseLine('test', str) == 'test'




#################################################################################
#################################################################################
## LINESFUNC 
#################################################################################
#################################################################################



def linesFunc(inLines):
    def gen(lines): 
        for l in lines: yield l
    g = gen(inLines)
    
    def tmins(tstr):
        h,m = tstr.split(':')
        return int(h) * 60 + int(m)

    caseCnt = parseLine(g.next(), int)
    for i in xrange(caseCnt):
        ttMin = parseLine(g.next(), int)
        na,nb = parseLine(g.next(), int, int)
        
        aTimes = [(parseLine(g.next(), str,str)) for i in xrange(na)]
        bTimes = [(parseLine(g.next(), str,str)) for i in xrange(nb)]
        aTimes = [(tmins(t1),tmins(t2)) for t1,t2 in aTimes]
        bTimes = [(tmins(t1),tmins(t2)) for t1,t2 in bTimes]
        
        print "%d %d %d" % (ttMin,na,nb)
        outputCase("%d %d" % calc(ttMin,aTimes,bTimes))

run('B', linesFunc, skipFirstLine=False)
