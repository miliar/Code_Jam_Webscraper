#!/usr/local/bin/python

# GOOGLE CODE JAM
# This is a submission to the Google Code Jam 2013


import sys
import os
import re
import math

#####################################################################
####                        SETTINGS                             ####
#####################################################################


#bool - Defines wether test mode should be used regardless of arguments
        # Useful for debugging in an IDE, make sure to set it back
FORCE_TEST_MODE = False

#str - Test Input 
      #Just like a real code jam File
      #maybe put the sample input in a file 
      #and read it here
TEST_INPUT = open("test.txt","rU").read()

#list - Expected utputs for each test case
        #Without Case #x: 
        #make sure len of this == number of problems in input
TEST_OUTPUT=["1 0","1 0","1 1", "0 0", "500 499"]

#bool - Defines wether the number of lines per test case is constant or not
        #This will be stated in the problem description
        #If false, you need to have a look at parseInput
NR_OF_LINES_PER_CASE_ISCONSTANT = True

#int - Number of lines per case, if NR_OF_LINES_PER_CASE_ISCONSTANT = True
      #Most of the times this is 1 if not otherwise stated int the problem desc
NR_OF_LINES_PER_CASE = 1



#####################################################################
####                        YOUR CODE HERE                       ####
#####################################################################



#Parses the input file 
#ONLY EXECUTED if not NR_OF_LINES_PER_CASE_ISCONSTANT
#input = list of string with lines in the input file excluding the first
#problemCount = Ammount of problems in input "first line"

#Returns list of list of strings of test cases
def parseInput(input, problemCount):
  #Example Implementation:
  #   one line at the beginning of every
  #   problem with an int that represents
  #   the number of lines per problem

  cases = []
  for x in xrange(0,problemCount):
    count = input[0]
    curCase = []
    for line in xrange(0,int(count)+1):
      curCase.append(input.pop(0))
    cases.append(curCase)
  return cases







#Main problem solving

#case = list of string with lines in input file
#       that belong to one Test case
#Returns output for the case as string; Unformatted (no Case: #X)
#   and without \n
def solveCase(case):
  n = int(case[0].split(" ")[0])
  k = int(case[0].split(" ")[1])
  s = [False] * n
  mins = 0
  maxs = 0
  for m in range(1,k+1):
    #print "Person " + str(m)
    sl = getsl(s)
    sr = getsr(s)

    best = map(lambda a,b:min([a,b]), sl,sr)
    #print best
    bestind = getindices(max(best), best)
    #print bestind

    if len(bestind)==1:
      s[bestind[0]] = True
      mins = min([sl[bestind[0]], sr[bestind[0]]])
      maxs = min([sl[bestind[0]], sr[bestind[0]]])

      continue

    second = map(lambda a: max([sl[a],sr[a]]), bestind)
    #print second
    secondind = getindices(max(second), second)
    #print secondind, bestind[secondind[0]]
    s[bestind[secondind[0]]] = True
    mins = min([sl[bestind[secondind[0]]], sr[bestind[secondind[0]]]])
    maxs = max([sl[bestind[secondind[0]]], sr[bestind[secondind[0]]]])

  return str(maxs-1) + " " + str(mins-1)




def getindices(o,l):
  return [i for i, x in enumerate(l) if x == o]


def getsl(s):
  l = 0
  sl = [0] * len(s)
  i = 0
  for t in s:
    if not t:
      l+=1
      sl[i] = l
    else:
      l = 0
    i += 1
  return sl


def getsr(s):
  l = 0
  sl = [0] * len(s)
  i = 0
  for t in reversed(s):
    if not t:
      l+=1
      sl[i] = l
    else:
      l = 0
    i += 1
  return list(reversed(sl))

######################################################################
#####ONLY BOILERPLATE CODE BELOW - SHOULD NOT NEED TO BE ALTERED #####
######################################################################


def getCases(lines):
  # Parse file
  cases = []
  try:
    m = int(lines.pop(0)) #Number of problems always in line 
  except Exception, e:
    errorOut("Invalid Input")


  if NR_OF_LINES_PER_CASE_ISCONSTANT:
    n = NR_OF_LINES_PER_CASE
    i = 0

    for x in xrange(0,m):
      case = []
      for x in xrange(0,n):
          case.append(lines.pop(0))
      cases.append(case)

  else:
    cases = parseInput(lines,m)

  print "Found "+str(len(cases))+" test cases\n"
  return cases



## Work with unit tests - define TEST_INPUT : see above
def test():
  
  if not TEST_INPUT and not TEST_OUTPUT:
    errorOut("Please make sure you define TEST_INPUT and TEST_OUTPUT")
  testcount = len(TEST_OUTPUT)
  rightcount = 0
  

  cases = getCases(TEST_INPUT.split("\n"))
  solutions = TEST_OUTPUT

  if not len(cases) == testcount:
    errorOut("Invalid test cases")

  i=0
  for testcase in cases:
    toprint = "Evaluating: "
    solve = solveCase(testcase)
    if solve==solutions[i]:
      toprint += "Correct!"
      rightcount+=1
    else:
      toprint+="Uh oh!"
    
    toprint += "   Given: "+solve
    toprint += " Expected: "+solutions[i]
    toprint += " Input: "+ "\\n".join(testcase)
    print toprint 

    i+=1

  print
  print "Solved "+str(rightcount)+" out of "+ str(testcount) + " test cases correctly"



def production():
  # Get filename
  #Default filename = SCRIPT.in (Without .py)  
  filename = sys.argv[0][:-3]+".in"
  if "--in" in sys.argv:
    try:
      filename=sys.argv[sys.argv.index("--in")+1]
    except Exception, e:
      errorOut("Please specify an input file")
    

  if not os.path.isfile(filename):
    errorOut("Specified input file does not exist\nStandard input: "+sys.argv[0][:-3]+'.in\n')

  # Get output file
  out=sys.argv[0][:-3]+".out"
  if "--out" in sys.argv:
    try:
      out=sys.argv[sys.argv.index("--out")+1]
    except Exception, e:
      errorOut("Please specify an output file")
    
  
  # Get input by line
  f=None
  try:
    f=open(filename,"rU")
  except Exception, e:
    errorOut("Could not open input file!")

  cases = getCases(f.read().split("\n"))


  
  # Let's play

  output = ""
  curCase = 1
  for case in cases:
    print "Solving " + str(curCase) + " out of "+str(len(cases))
    output+="Case #"+str(curCase)+": "
    output+=solveCase(case)
    output+="\n"
    curCase+=1
 

  # Store output
  try:
    outf = open(out,"w")
    outf.write(output)
    outf.close()

    print "\n\n"

    print "Done! Output stored in: "+out
  except Exception, e:
    print "Error writing output! Here it is in stdout \n"+output

def main():
  if "--test" in sys.argv or FORCE_TEST_MODE:
    print "Test mode"
    test()
  else:
    print "Production mode"
    production()
    


#Exit with error
def errorOut(msg):
  sys.stderr.write(msg+"\n")
  sys.exit(1)

if __name__ == '__main__':
  main()
