#!/usr/bin/env python2.6
# A submission by Cortland Klein <me@pixelcort.com>


from pdb import set_trace
import re
import sys

def computeAnimalProbabilityWithRealTree(animal,realTree):
  if isinstance(realTree, list):
    if len(realTree) == 1:
      return computeAnimalProbabilityWithRealTree(animal,realTree[0])
    
    elif len(realTree) == 4:
      if realTree[1] in animal:
        subProb = computeAnimalProbabilityWithRealTree(animal,realTree[2])
      else:
        subProb = computeAnimalProbabilityWithRealTree(animal,realTree[3])
      return subProb * float(realTree[0])
    else:
      print "ERROR: WAS NOT 1 or 4"
  elif isinstance(realTree,str):
    return float(realTree)
  else:
    set_trace()
    print "ERROR: WAS NOT LIST NOR STRING"

filename = sys.argv[1]
with open(filename) as f:
  with open(filename+'out','w') as out:
    n = long(f.next())
    for i in range(n):
      l = long(f.next())
      treeText = [f.next() for blah in range(l)]
      treeSymbolsGrid = [blah.split() for blah in treeText]
      def flatten(l): #http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html
        out = []
        for item in l:
          if isinstance(item, (list, tuple)):
            out.extend(flatten(item))
          else:
            out.append(item)
        return out
      treeSymbolsFlat = flatten(treeSymbolsGrid)
      treeSymbols = []
      for chunkSymbol in treeSymbolsFlat:
        currentSymbol = []
        for character in chunkSymbol:
          if character == '(' or character == ')':
            treeSymbols.append(''.join(currentSymbol))
            treeSymbols.append(character)
            currentSymbol = []
          else:
            currentSymbol.append(character)
        treeSymbols.append(''.join(currentSymbol))
      
      def buildTree(slice):
        # print slice
        subRangePointer = 0
        inASubRange = 0
        ret = []
        for offset in range(len(slice)):
          symbol = slice[offset]
          if symbol == '':
            continue
          elif symbol == '(':
            inASubRange = inASubRange + 1
            if inASubRange == 1:
              subRangePointer = offset+1 # Don't include the opening bracket
          elif symbol == ')':
            inASubRange = inASubRange - 1
            if inASubRange == 0:
              # print subRangePointer
              ret.append(buildTree(slice[subRangePointer:offset]))
          elif not inASubRange:
            ret.append(symbol)
        return ret
      
      
      realTree = buildTree(treeSymbols)
      
      out.write("Case #" + str(i+1) + ":" + "\n")
      # Get the Animals
      a = long(f.next())
      for j in range(a):
        animal = [blah for blah in f.next().split()]
        animal.pop(0) # Don't need the name
        animal.pop(0) # Don't need the length of attributes
        
        probability = computeAnimalProbabilityWithRealTree(animal,realTree)
        out.write("%.8F\n" % probability)

