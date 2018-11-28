import sys

def dbg(s):
  sys.stderr.write( "%s\n" % s )
  #pass

found = 0
sentence = ''

def rdfs( nextpos, lastpos ):
  global found, target, sentence
  # find next letter
  next = sentence.find( target[nextpos:nextpos+1], lastpos+1)
  while next != -1: # found
    #dbg( "found %i: %s in %s" % (nextpos, target[nextpos:nextpos+1], sentence[lastpos+1:] ) )
    # success?
    #dbg( "nextpos: %i len: %i" % ( nextpos, len(target)))
    if nextpos == target_len-1:
      found += 1
      if found == 10000:
        found = 0
      #rdfs( nextpos, next ) # keep looking with same
    else:
      rdfs( nextpos+1, next ) # next in target
    next = sentence.find( target[nextpos:nextpos+1], next+1)
  #dbg( "notfound %i: %s in %s" % (nextpos, target[nextpos:nextpos+1], sentence[next+1:] ))
  # no more


def dfs( sent ):
  global found, sentence
  found = 0
  sentence = sent
  rdfs( 0, -1 )
  return found


target = "welcome to code jam"
target_len = len(target)

i = open( "C-small.in" )
#i = open( "quala-eg.in" )

c = int(i.readline().strip())

dbg( "solving %i" % c )
for idx in xrange(1,c+1):
  current = i.readline().strip()
  matches = dfs( current )
  #dbg( "Case #%i: %i" % (idx, matches) )
  print "Case #%i: %04i" % (idx, matches%10000)

