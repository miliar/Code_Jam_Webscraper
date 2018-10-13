import sys

def dbg(s):
  sys.stderr.write( "%s\n" % s )
  #pass

i = open( "A-large.in" )
#i = open( "quala-eg.in" )

f = i.readline().strip()
(l, d, n) = f.split( ' ' )
l = int(l)
d = int(d)
n = int(n)

w = set()
index = set()
for idx in xrange( 0, d ):
  next = i.readline().strip()
  w.add( next )
  for p in xrange( 1, len(next) ):
    index.add( next[0:p] )

found = 0

def rdfs( bits, level, pre ):
  global found, w, index
  levels = len(bits)
  s = []
  for c in bits[level]: # for each level
    s.append( c )
    current = pre + ''.join(s)
    #dbg( "current: %s" % current )
    if level == levels-1: # at end
      if current in w:
        found += 1
    else: # next level
      if current in index:
        rdfs( bits, level+1, current )
      #else:
        #dbg( "skipping: %s not in index" % current )
      # else skip
    s.pop()

def dfs( bits ):
  global found
  found = 0
  rdfs( bits, 0, '' )
  return found

dbg( "solving %i" % n )
for idx in xrange( 1, n+1 ):
  next = i.readline().strip()
  # break into bits
  bits = next.split( ")" )
  #dbg( bits ) 
  newbits = []
  for bit in bits:
    if len(bit) == 0:
      continue
    #dbg( "bit is %s" % bit )
    if bit.find( '(' ) != -1:
      m = bit.find( '(' )
      for b in bit[0:m]:
        newbits.append(b)
      newbits.append( bit[m+1:] )
    else:
      for b in bit:
        newbits.append(b)
    #dbg( "newbit is %s" % newbits )
  # find words matching bits
  #dbg( newbits )
  matches = dfs( newbits )
  dbg( "Case #%i: %i" % (idx, matches) )
  print "Case #%i: %i" % (idx, matches)
  
