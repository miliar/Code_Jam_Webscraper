#!/usr/bin/env python
import sys,os
import numpy as np

mymod=1000002013

def journeyCost(i,j,N):
    dx=abs(i-j)
    return (dx*N+dx-(dx*(dx+1))/2)%mymod

def Solve(N,M,J):
    tot=0

    J.sort()

    for p in J:
        tot += (journeyCost(p[0],p[1],N)*p[2])%mymod

    getOn,getOff={},{}

    for p in J:
        if p[0] not in getOn: getOn[p[0]]=0
        if p[1] not in getOff: getOff[p[1]]=0
        getOn[p[0]]+=p[2]
        getOff[p[1]]+=p[2]

    allStops=sorted( set(getOn.keys()).union( set(getOff.keys())) )
    #print 'Tot',tot

    profit=0
    ticketsFrom={}
    for stop in allStops:
        if stop in getOn:
            ticketsFrom[stop]=getOn[stop]

        if stop in getOff:
            froms=ticketsFrom.keys()
            froms.sort(reverse=True)
            toGetOff=getOff[stop]
            for f in froms:
                if toGetOff==0: break

                if ticketsFrom[f]>toGetOff:
                    #print toGetOff,'went from %d to %d'%(f,stop),\
                    ticketsFrom[f] -= toGetOff
                    profit+=(journeyCost(f,stop,N)*toGetOff)%mymod
                    toGetOff=0
                    #print profit
                    break
                else:
                    #print ticketsFrom[f],'WENT from %d to %d'%(f,stop),\

                    profit+=(journeyCost(f,stop,N)*ticketsFrom[f])%mymod
                    #print profit,journeyCost(f,stop,N),ticketsFrom[f]

                    toGetOff -= ticketsFrom[f]
                    del ticketsFrom[f]
            else:
                if toGetOff!=0: raise ValueError(toGetOff)
            #print toGetOff

    #print ticketsFrom
                
    return (tot-profit)%mymod



def parse(infile):
    N,M=map(int, infile.readline().split() )
    pairs=[]
    for i in xrange(M):
        pairs.append(map(int, infile.readline().split() ))
    return N,M,pairs



class GCJ_Parser( object ):
    def __init__(self,fname):
        self.infile=open(fname,'r')
        self.NumCases=int(self.infile.readline().strip() )
        self.caseNum=0

    def __iter__(self): return self

    def next(self):
        if self.caseNum==self.NumCases: raise StopIteration
        self.caseNum += 1
        args=parse(self.infile)
        return self.caseNum , args


def runmain():
    myCases=GCJ_Parser(sys.argv[1])

    #Open output file, but don't overwrite old ones (for comparison)
    outname=sys.argv[1].rstrip('.in')+'.out'
    if os.path.isfile(outname):
        oldout=outname+'.old'
        ii=0
        while os.path.isfile(oldout):
            ii+=1
            oldout=outname+'.old'+str(ii)
        os.rename(outname,oldout)
        print 'Rename: %s -> %s'%(outname,oldout)   
 
    outfile=open(outname,'w')

    for iCase, args in myCases:
        answer=Solve(*args)

        print 'Case #'+str(iCase)+':',answer
        print >> outfile, 'Case #'+str(iCase)+':',answer




if __name__=='__main__':
    runmain()
