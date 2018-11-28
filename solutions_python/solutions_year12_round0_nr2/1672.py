#!/usr/bin/python
# python 2.x (tested on 2.7)

# author: Alexej Fink, fink.alexej@googlemail.com
# 2012-04-14

import sys

#====================================================================

def calc_triples( case, surprizeCount, limit, scores, log=False):
  if log: print "=== Calculate triples for ", len(scores), " goolers, with ", surprizeCount, " surpize scorings for ", limit, " as minimal border"
  
  surprizesLeft= surprizeCount
  p= 0

  for total in scores:
    low= total / 3;
    
    if low >= limit:
      p+=1
      continue
    
    if low+2 < limit:
      continue
    
    diff= total - low*3
    if low+1 == limit:
      if diff > 0:
	p+=1
	continue
      if surprizesLeft > 0 and low > 0:
	p+=1
	surprizesLeft-=1
	continue

    if low+2 == limit and surprizesLeft > 0 and diff == 2:
      p+=1
      surprizesLeft-=1
      continue
    
  if log: print "[W] unhandled situation!"
  if log: print "    total:",total, ", suprizes:",surprizeCount,", left:",surprizesLeft,", low:",low,", limit: ",limit
  if log: print "[I] total:",total, ", suprizes:",surprizeCount,", left:",surprizesLeft,", p:",p,",  scores:",scores
  print "Case #" + str(case) + ": " + str(p)
  return p
  
#====================================================================

def calc_triples_for_line( case, line, log=False):
  all= line.split()
  allDig= [int(a) for a in all]
  N= allDig[0]
  S= allDig[1]
  p= allDig[2]
  scores= allDig[3:]
  if len(scores) != N:
    print "[E] Invaild entry in data file: " << line
    return -1
  p= calc_triples( case+1, S, p, scores, log)
  return p

def calc_triples_for_file( infile, outfile=None, result=None):
    
  if outfile is not None:
    outfile.write( "Case #" + str(l+1) + ": " + str(p) + "\n")
  
#====================================================================

tstdata="""4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21""";
tstresult=[3,2,1,3];
	
if __name__ == "__main__":
  
  if not sys.version.startswith("2."):
    print "This script requires python version 2.x"
    sys.exit(1)
  
  if len(sys.argv) > 3:
    print "USAGE:",sys.argv[0]," infile [outfile]"
    sys.exit(1)
    
  # testcases
  
  print "=== Do the tests ==="
  tsts= tstdata.split('\n')
  lines= tsts[1:]
  case= 0
  for line in lines:
    p= calc_triples_for_line( case, line)
    if p != tstresult[case]:
      print "[E] Test failed! "
      calc_triples_for_line( case, line, True)
      sys.exit(1)
    case+= 1
  
  # load dynamic data
  
  if len(sys.argv) == 1:
    sys.exit(0)
    
  print "=== Process input data ==="
  
  f = open( sys.argv[1], 'r')
  lineCount= int(f.readline())
  
  outfile= None
  if len(sys.argv) == 3:
    outfile= open( sys.argv[2], 'w')
    print "[i] write output to", sys.argv[2]

  case= 0
  for l in range(lineCount):
    line= f.readline()
    p= calc_triples_for_line( case, line)
    case+= 1
    if not outfile is None:
      outfile.write("Case #" + str(case) + ": " + str(p) + "\n")

  if not outfile is None:
    outfile.close()
  
#====================================================================
