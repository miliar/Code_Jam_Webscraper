#!/usr/bin/python -O

import sys
import os

def main(argv=None):

  debug = False

  def doInvoke(inv,com,opp):
    if debug:
      print "doInvoke"
    tail = inv[-2:]
    tail_aux = tail[:]
    tail_aux.reverse()
    u = ''.join(tail)
    v = ''.join(tail_aux)
    if debug:
      print "tail:" + u, ", rev tail: " + v
      print "com:" + str(com), ", opp: " + str(opp)
    if len(com):
      if u in com:
        if debug:
          print "Combining..."
        inv = inv[0:-2]
        inv.append(com[u])
        if debug:
          print inv
        return inv
      elif v in com:
        if debug:
          print "Combining..."
        inv = inv[0:-2]
        inv.append(com[v])
        if debug:
          print inv
        return inv
    if len(opp): 
      if debug:
        print "Oppose.."
      if len(inv) > 2:
        for e in inv[0:-1]: 
      	  key1 = ''.join([e,inv[-1]])
          key2 = ''.join([inv[-1],e])
          if key1 in opp or key2 in opp:
            inv = [] 
            break
      else:
        if u in opp or v in opp:
          inv = inv[0:-2]
    return inv

  if argv is None:
    argv = sys.argv

  try: 
    f = open(sys.argv[1], 'r')
  except IndexError as e:
    print "Please specify an input file"
    return 127
  except IOError as e:
    print "Could not read file!"
    return 127

  n = int(f.readline())
  n_case = 1

  while n_case <= n:
    testcase = f.readline().split()
    combine = []
    oppose = []
    result = []
    c = int(testcase[0])
    d = 0
    if c:
      combine = dict((x[:-1],x[-1]) for x in testcase[1:c+1])
    d = int(testcase[c+1])
    if d:
      oppose = testcase[c+2:c+2+d]
    s = int(testcase[c+2+d])
    invoke = testcase[c+2+d+1:]

    if debug:
      print "Test Case: " + str(testcase)
      print "Combine: "+ str(combine)
      print "Oppose: "+ str(oppose)
      print "Elements: "+ str(invoke)

    for elem in list(invoke[0]):
      if debug: 
        print "Next element: " + str(elem)
      result.append(elem)
      if len(result) > 1:
        result = doInvoke(result,combine,oppose)
    print "Case #" + str(n_case) + ': ' + '[' + ', '.join(result) + ']'
    n_case += 1
  f.close()
  return 0

      
if __name__ == "__main__":
    sys.exit(main())
