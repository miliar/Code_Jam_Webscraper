#coding:utf8
import sys
import psyco
psyco.full()
from benchmarker import Benchmarker
from collections import defaultdict
from Queue import PriorityQueue

def main():
  global infile
  global out_file
  debug = False
  in_filename = sys.argv[1]
  out_filename = sys.argv[2]
  if len(sys.argv)>=4:
    debug = True
  in_file = open(in_filename, 'r')
  out_file = open(out_filename, 'w')
  
  bm = Benchmarker()
  #if 1:
  with bm('process'):
    t = get_next_int(in_file)
    
    results = []
    for step in xrange(int(t)):
      n, m = get_nexts_int(in_file)
      travels = [get_nexts_int(in_file) for i in xrange(m)]
      answer = solve(n,travels)

      results.append(answer)
    print_out_int(results, out_file,debug)

def solve(n,travels):
  q = PriorityQueue()
  normal_gains = 0
  
  for o, e, p in travels:
    distance = e - o
    normal_gains += ( n * distance - (distance * (distance+1) / 2 )) * p
  
  enters = defaultdict(int)
  exits = defaultdict(int)
  
  for o, e, p in travels:
    enters[o] += p
    exits[e] += p
  
  swap_gains = 0
  for i in xrange(1,n+1):
    if i in enters:
      for j in xrange(enters[i]):
        q.put(i*-1)
    if i in exits:
      for j in xrange(exits[i]):
        distance = i - (q.get() * -1)
        swap_gains += ( n * distance - (distance * (distance+1) / 2 ))
  
  return normal_gains - swap_gains
  

def get_next(f):
  line = f.readline()
  return line.rstrip('\n')
def get_nexts(f):
  line = f.readline()
  return line.rstrip('\n').split(" ")

def get_next_int(f):
    return int(get_next(f))

def get_nexts_int(f):
    return map(int, get_nexts(f))
def get_nexts_float(f):
    return map(float, get_nexts(f))
    
def get_nexts_digit(f):
    return map(int, list(get_next(f)))

def print_out(results, out_file, debug=False):
  for i, result in enumerate(results):
    num = i + 1
    print >>out_file, "Case #%d:\n%s" % (num, result )
    if debug:
        print "Case #%d:\n%s" % (num, result )
def print_out_int(results, out_file,debug=False):
  for i, result in enumerate(results):
    num = i + 1
    print >>out_file, "Case #%d: %s" % (num, result )
    if debug:
        print "Case #%d: %s" % (num, result )
    #print  "Case #%d: %s" % (num, result)

if __name__ == '__main__':
  main()
