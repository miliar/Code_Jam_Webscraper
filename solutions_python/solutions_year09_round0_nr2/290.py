#!/usr/bin/python

###############################################################################
#
# Google Code Jam 2009 - Qualification Round B
#
# Author: Andres Ayala
# email: killerrex@gmail.com
# License: GPL3
#
# Usage:
#   > qual_b.py input_file
#
#   input_file: File with the format specificated in the problem
#               No sanity checks are done over this files
#
###############################################################################

from sys import argv

Names = 'abcdefghijklmnopqrstuvwxyz'
#DBG Directions = [ 'North', 'West', 'East', 'South' ]

###############################################################################
# Cell class
class cell():
  """
  Just encapsulate a cell element with it's height, obtain the direction, slope...
  """
  def __init__(self, height):
    """
    Initialize only to a height
    """
    self.height = height
    self.flow = None
    self.letter = None
#DBG    self.dir = None 
    
  def __str__(self):
    """
    Some nice output
    """
    if self.letter is None:
      return "?"
    else:
      return self.letter
  
  def assign_name(self, ind):
    """
    If it is a sink, get the name, or do nothing.
    Otherwise try to label it sink get the letter form it.
    Return the next letter index
    """
    if self.letter is not None:
      return ind
    
    if self.flow is None:
      self.letter = Names[ind]
      ind+=1
    else:
      if self.flow.letter is None:
        ind = self.flow.assign_name(ind)
      self.letter = self.flow.letter
    return ind
  
  def find_flow(self, North, West, East, South):
    """
    Obtain the cell to flow to.
    After calling to this function if the flow continue being None, it is a sink
    Return True if it is a sink
    """
    best = 0
#DBG    ind = 0
    # The preference order is fixed by the order in the tuple
    # and the use of Delta>best instead of Delta>=best
    # so in case of tie the flow cell will be the 
    for c in (North, West, East, South):
      if c is not None:
        Delta = self.height - c.height
        if Delta>best:
          self.flow = c
          best = Delta
#DBG          self.dir = Directions[ind]
#DBG      ind +=1
    return self.flow is None
  
#DBG  def show_dir(self):
#DBG    """
#DBG    For debugging purposes only: Plot the flow direction
#DBG    """
#DBG    
#DBG    dChar = {'North':'A', 'West':'<', 'East':'>', 'South':'V'}
#DBG    if self.flow is None:
#DBG      return '#'
#DBG    else:
#DBG      return dChar[self.dir]
    
    


###############################################################################
# Area class
class Area():
  """ Define an area of HxW cells """
  def __init__(self, H, W, heights):
    """
    Initialize the area from an array of HxW heights
    Note: No sanity checks are done... we trust our user
    """
    self.H = H
    self.W = W
    self.area = [ [cell(h) for h in row] for row in heights ]
    self.N = None # Number of sinks
    
  def __str__(self):
    """
    Nice print
    """
    s = ''
    for row in self.area:
      s+='\n'
      nxt = ""
      for c in row:
        nxt += str(c) + " "
      s += nxt[0:-1]
    return s
    
  def find_flow(self):
    """
    Find a flow direction for each cell
    From the cell k,l the directions of the neighbors are
    North ==> k-1, l
    West  ==> k  , l-1
    East  ==> k  , l+1
    South ==> k+1, l
    """
    self.N = 0
    for k in xrange(self.H):
      for l in xrange(self.W):
        # First find out the neighborhoods
        if k==0:
          North = None
        else:
          North = self.area[k-1][l]
        
        if l==0:
          West = None
        else:
          West = self.area[k][l-1]
        
        if l==self.W-1:
          East = None
        else:
          East = self.area[k][l+1]
        
        if k==self.H-1:
          South = None
        else:
          South = self.area[k+1][l]
          
        if self.area[k][l].find_flow(North, West, East, South):
          self.N +=1
    return self.N

  def set_name(self):
    """
    Assign the names to the sinks according to the problem requirements
    """
    ind = 0
    for k in xrange(self.H):
      for l in xrange(self.W):
        ind = self.area[k][l].assign_name(ind)
    return
    
#DBG  def show_dirs(self):
#DBG    """
#DBG    Debug only
#DBG    """
#DBG    s = ''
#DBG    for row in self.area:
#DBG      s+='\n'
#DBG      for c in row:
#DBG        s += c.show_dir()
#DBG    return s
    


###############################################################################
# Read the file and do the print
def readsample(fName):
  fd = open(fName,"r")
  data = [ l.strip('\n') for l in fd.readlines() ]
  fd.close()
  
  T = int(data[0])
  
  nLine = 1
  for k in xrange(0,T):
    (H,W) =  (int(x) for x in data[nLine].split())
    nLine+=1
    heights = [ [ int(h) for h in row.split()] for row in data[nLine:nLine+H] ]
    nLine+=H
    A = Area(H, W, heights)
    A.find_flow()
#DBG    print "DBG:" + A.show_dirs()
    A.set_name()
    
    print "Case #%d:" % (k+1) + str(A)


###############################################################################
if __name__ == '__main__':

  if len(argv)==2:
    readsample(argv[1])
    
  else:
    print 'Usage: ' + argv[0] + ' input_file\n'

