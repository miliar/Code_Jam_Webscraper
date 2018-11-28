#!/usr/bin/python
from operator import attrgetter
from operator import itemgetter

import sys

class tc:

  def __init__(self,tcIndex,instr):
    self.myIndex = tcIndex
    self.N = int(instr.readline().strip())
    self.minTurns = 0

  def intToStr(self,N):
    return str(N)

  def strToInt(self,istr):
    if ( isinstance(istr,list) ): return int(''.join(istr))
    else:                         return int(istr)

  def runNTo(self,v):
    if ( isinstance(v,int) ):
      print 'Running N from %i to %i' % ( self.curN, v)
      self.minTurns += (v - self.curN)
      self.curN = v
    elif ( isinstance(v,str) ):
      print 'Running N from %i to %s' % ( self.curN, v)
      self.minTurns += (self.strToInt(v) - self.curN)
      self.curN = self.strToInt(v)
  def revN(self):
    
    oldN = self.curN
    ss = self.intToStr(self.curN)
    ss = ss[::-1]
    self.curN = self.strToInt(ss)
    if ( oldN != self.curN ):
     self.minTurns += 1
     print 'Reversing N from %i to %i' % ( oldN, self.curN)


  def solve(self):
    if ( self.N < 10 ):
      self.minTurns = self.N
      return
    self.curN = 1
    self.minTurns = 1
    self.runNTo(10)
    print self.curN
    curDigN = 2
    nextDecN = self.curN*10
    counts = 1
    # first round out the decades
    goalDigN = len(self.intToStr(self.N))
    while ( curDigN < goalDigN ):
      targetStr = [c for c in self.intToStr(self.curN)]
      for sweepDig in range(0,int(curDigN/2)):
        targetStr[-(sweepDig+1)] = '9'
      self.runNTo(''.join(targetStr))
      self.revN()
      self.runNTo(nextDecN)
      nextDecN = self.curN*10
      curDigN += 1
    if ( self.curN == self.N ): return

    finalStr  = [c for c in self.intToStr(self.N   )]
    targetStr = [c for c in self.intToStr(self.curN)]
    print 'Got from %s to %s' % (targetStr,finalStr)
    for sweepDig in range(0,int(curDigN/2)):
      #print '%i %s %s' % (sweepDig,targetStr[-(sweepDig+1)] , finalStr[sweepDig] )
      if    ( targetStr[-(sweepDig+1)] <= finalStr[sweepDig] ) \
        and (      targetStr[sweepDig] <= finalStr[sweepDig] ):
        targetStr[-(sweepDig+1)] = finalStr[sweepDig]
    revTurn = ( self.strToInt(targetStr[::-1]) - self.strToInt(targetStr) ) + 1 \
             + (self.strToInt(targetStr) - self.curN)
    strTurns = self.N - self.curN
    print 'Target now %s' % targetStr
    if ( revTurn < strTurns ):
      self.runNTo(''.join(targetStr))
      self.revN()
    self.runNTo(self.N)

  def share(self,ostr):
    ostr.write ( 'Case #%i: %i\n' % (self.myIndex,self.minTurns) )

def main():
  numTC = int(sys.stdin.readline().strip())
  for tci in range(0,numTC):
    theTC = tc(tci+1,sys.stdin)
    theTC.solve()
    theTC.share(sys.stdout)


main()
