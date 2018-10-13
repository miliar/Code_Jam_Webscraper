#!/usr/bin/python
import string

allTheLetters = string.lowercase

def debug(message):
  print message



def convertChar(char):
  

  for m in charMap:
    if m[0]==char:
      return m[1]
  debug("could not find "+char)
  
  #charMap.append([char,shouldBe]);
  

print "start"

outfile=open('out','w')


infile=open('in','r')


charMap=[['e', 'o'], ['j', 'u'], ['p', 'r'], [' ', ' '], ['m', 'l'], ['y', 'a'], ['s', 'n'], ['l', 'g'], ['c', 'e'], ['k', 'i'], ['d', 's'], ['x', 'm'], ['v', 'p'], ['n', 'b'], ['r', 't'], ['i', 'd'], ['b', 'h'], ['t', 'w'], ['a', 'y'], ['h', 'x'], ['w', 'f'], ['f', 'c'], ['o', 'k'], ['u', 'j'], ['g', 'v'], ['q', 'z'], ['z', 'q'] ]



infile.readline()

caseNumber=0

for line in infile:

    caseNumber+=1
    
    line=line.rstrip('\n');
    
    #debug("line is"+line)
    
    convertedLine=""
    
    for i, c in enumerate(line):
      convertedLine += convertChar(c)
    
    outLine="Case #"+str(caseNumber)+": "+convertedLine
    
    print outLine
    outfile.write(outLine+"\n")

print charMap;
print len(charMap)




def checkLetter(l):
  for m in charMap:
    if m[0]==l:
      return
  print "could not find "+ l


def checkLetter2(l):
  for m in charMap:
    if m[1]==l:
      return
  print "could not find 2 "+ l



for l in allTheLetters:
  checkLetter(l)


for l in allTheLetters:
  checkLetter2(l)







