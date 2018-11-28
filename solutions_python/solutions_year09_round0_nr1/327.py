#!/usr/bin/python

###############################################################################
#
# Google Code Jam 2009 - Qualification Round A
#
# Author: Andres Ayala
# email: killerrex@gmail.com
# License: GPL3
#
# Usage:
#   > qual.py input_file
#
#   input_file: File with the format specificated in the problem
#               No sanity checks are done over this files
#
###############################################################################



from sys import argv

###############################################################################
# Candidate word
class candidate():
  """
  Candidate: Process a string from the input as a candidate.
  It manage correctly the (), allow for direct indexing of a group.
  """
  def __init__(self, txt):
    """
    Initialize the candidate from a string.
    """
    self.options = []
    k = 0
    while (k<len(txt)):
      if '(' == txt[k]:
        k+=1
        k2 = txt.find(')',k)
        if ((-1 == k2) or (k2<=k)): raise ValueError('Incorrect input string: ' + txt)
        self.options.append(txt[k:k2])
        # Advance after the )
        k = k2+1
      elif txt[k].islower():
        self.options.append(txt[k])
        k+=1
      else:
        raise ValueError('Incorrect input string: ' + txt)
      
      self.L = len(self.options)
    
  def __str__(self):
    """
    Just some pretty printing
    """
    return 'Candidate: ' + str(self.options)
    
  def __getitem__(self, k):
    """
    Allow easy access to the elements with []
    Don't caare about slices
    """
    return self.options[k]
  
  def __len__(self):
    """
    Just in case
    """
    return self.L
  
  

###############################################################################
# Alien dictionary
class aliendict():
  """
  Keeps a collection of words from the alien dictionary,
  reading them from a list of words.
  It also perform the intersection with a candidate to get the number of valid options
  """
  def __init__(self, lst):
    """
    Initialize the dictionary from a list of words.
    We thrust the user and assume all the words are of the same length.
    """
    self.words = lst;
  
  def __str__(self):
    """
    Just some pretty printing
    """ 
    return 'Alien: ' + str(self.words)
    
  def evaluate(self, cnd):
    """
    Evaluate the posibilities of a word to be part of the dictionary
    """
    
    # Create a copy of the dictionary so we can reduce if afterwards
    cpy = self.words[:]
    for k in xrange(0,len(cnd)):
      cpy = [ w for w in cpy if w[k] in cnd[k]] # Some list magic. Filter all the words that does not match the group k
      N = len(cpy)
      if N==0:
        break    
    return N
  

###############################################################################
# Read a file with a task
def readsample(fName):
  
  fd = open(fName,"r")
  data = [ l.strip('\n') for l in fd.readlines() ]
  fd.close()
  
  (L,D,N) = (int(x) for x in data[0].split())
  adict = data[1:D+1]
  sample = data[D+1:D+N+1]
  
  return (adict, sample)


###############################################################################
if __name__ == '__main__':
  
  if len(argv)==2:
    # Read the file, create the dictionary and evaluate the options of each sample... easy
    (words, Samples) = readsample(argv[1])
    aDict = aliendict(words)
    
    k = 1
    for s in Samples:
      cnd = candidate(s)
      Opt = aDict.evaluate(cnd)
      print 'Case #%d: %d' % (k, Opt)
      k+=1
    
  else:
    print 'Usage: ' + argv[0] + ' input_file\n'

 


