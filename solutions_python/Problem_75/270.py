#!/usr/bin/python -tt
import sys


def magika():
  filename = sys.argv[1]
  input_file = open(filename, 'r')
  # get the number of cases
  num_of_cases = int(input_file.readline())
  for i in range(1, num_of_cases + 1):
    il = [x for x in list(input_file.readline().strip().split())]
    
    #list has all the cases in it now. Lets create the hashes.
    ophash = {}
    comhash = {}
  
    
    comhashsz = int(il.pop(0))
    if comhashsz != 0:
      for j in range(0, comhashsz):
        tmpl = list(il.pop(0))
        comhash[(tmpl[0], tmpl[1])] = tmpl[2]
        comhash[(tmpl[1], tmpl[0])] = tmpl[2]
  
  
    ophashsz = int(il.pop(0))
    if ophashsz != 0:
      for j in range(0, ophashsz):
        tmpl = list(il.pop(0))
        ophash[tmpl[0]] = tmpl[1]
        ophash[tmpl[1]] = tmpl[0]
    
    
    il.pop(0)  # I don't need number of spells invoked. Muhahaha. Loving Python
    
    tmpl = list(il.pop(0))
    finallst = []
    size = len(tmpl)
    
    for j in range(0, size):
      spell = tmpl[j]
      
      if len(finallst) > 0:
        spell2 = finallst.pop()
        if comhash.has_key((spell, spell2)):
          finallst.append(comhash[(spell, spell2)])
          continue
        else:
          finallst.append(spell2)
      
      if ophash.has_key(spell) and finallst.count(ophash[spell]) > 0:
        finallst = []
        continue
      
      
        
      finallst.append(spell)  
    
    sys.stdout.write ("Case #" + str(i) + ": " + "[")
    size = len(finallst)
    for j in range(0, size -1 ): 
      sys.stdout.write(str(finallst.pop(0)) + ", ")
    if (size):
      sys.stdout.write(str(finallst.pop(0)))
    print  "]"
          
       
 

if __name__ == '__main__':
  magika()