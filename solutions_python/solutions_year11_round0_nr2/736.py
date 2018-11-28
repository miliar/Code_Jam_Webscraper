import sys, re
  
class Solver:

  def char2int(self,C):
    ret = int(ord(C[0])-ord('A'))
    return ret

  def try_combine(self, C):
    if len(self.stack)==0:
      self.stack.append(C)    
      self.counts[self.char2int(C)]+=1
      return True      
    last = self.stack[len(self.stack)-1]
    if last in self.combine: 
      cmb = self.combine[last]
      for z in cmb:
        if C==z[0]:
          self.stack[len(self.stack)-1]=z[1]
          self.counts[self.char2int(last)]-=1
          self.counts[self.char2int(z[1])]+=1
          return True
    self.stack.append(C)
    self.counts[self.char2int(C)]+=1
    return False


  def try_opposed(self, C):
    if len(self.stack)==0:
      self.stack.append(C)
      self.counts[self.char2int(C)]+=1
      return False
    if C in self.opposed: 
      for z in self.opposed[C]:        
        if self.counts[self.char2int(z)]>0:
#          print self.stack, z, C, self.counts
          self.counts = [0 for x in range(0,26)]
          self.stack = []
          return True
    return False


  def main(self):  
    N = sys.stdin.readline()

    for case in range(0,int(N)):
      self.opposed = {}
      self.combine = {}
      self.counts = [0 for x in range(0,26)]
      self.stack = []
      seq = [x for x in sys.stdin.readline().split()]
  
      #combine
      N = int(seq[0])  
      for i in range(1,N+1): 
        str = seq[i]
        if not seq[i][0] in self.combine: self.combine[seq[i][0]]=[]
        self.combine[seq[i][0]].append(seq[i][1:3])
        if not seq[i][1] in self.combine: self.combine[seq[i][1]]=[]
        self.combine[seq[i][1]].append(seq[i][0]+seq[i][2]) 
      #opposed
      if N>0: seq = seq[N+1:len(seq)]
      else: seq = seq[1:len(seq)]
      N = int(seq[0])  
      for i in range(1,N+1): 
        #print seq[i]
        if not seq[i][0] in self.opposed: self.opposed[seq[i][0]]=[]
        self.opposed[seq[i][0]].append(seq[i][1])
        if not seq[i][1] in self.opposed: self.opposed[seq[i][1]]=[]
        self.opposed[seq[i][1]].append(seq[i][0])
      #sequence
      A = seq[len(seq)-1]

      for C in A:
        #print "zznak:", C 
        if not self.try_combine(C):
          #print "opp"
          self.try_opposed(C)
        #print self.stack
  
      ret = "["
      prv = True
      for s in self.stack:
        if prv:
          prv = False
          ret+=s
        else:
          ret+=", "+s
      ret+="]"
      print "Case #%d:" % (case+1),ret


s = Solver()
s.main()
