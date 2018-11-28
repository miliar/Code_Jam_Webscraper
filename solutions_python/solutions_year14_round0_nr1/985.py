#!/bin/python
import sys




def readin(infile):
  print >> sys.stderr, "reading from " + infile
  lines=open(infile, 'r').readlines()
  testcount = int(lines[0])
  print >> sys.stderr, "read %d test cases from %d lines"%(testcount, len(lines))
  lines=lines[1:]
  return testcount, lines

def doall(testcases, lines):
  case = 1

  while lines:
    choice1 = int(lines[0])
    data1 = [[int(n) for n in l.split()] for l in lines[1:5]] 
    lines=lines[5:]
    choice2 = int(lines[0])
    data2 = [set(int(n) for n in l.split()) for l in lines[1:5]] 
    lines=lines[5:]

    solve(case, choice1, data1, choice2, data2)
    case+=1

def solve(case, choice1, data1, choice2, data2):
  print 'Case #%d:'%case,
  possible = set(data1[choice1-1]) & set(data2[choice2-1])
  if len(possible)==0:
    print 'Volunteer cheated!'
  elif len(possible)>1:
    print 'Bad magician!'
  else:
    print possible.pop()


if __name__ == '__main__': 
  if len(sys.argv) != 2:
    print >> sys.stderr, "bad args"
    sys.exit(1)
  tc, l = readin(sys.argv[1])
  doall(tc, l)
  print >> sys.stderr, "done"

