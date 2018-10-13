tx = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
tx['z'] = 'q'

f = open( "1", "r" )
l = f.readlines()

tests = int(l[0])

def convert( f ):
  result = []
  for c in f:
    if tx.has_key( c ):
      result.append( tx[c] )
    else:
      result.append( c )
  return ''.join( result )

for i in xrange(1, tests+1):
  line = l[i].strip()
  result = convert( line )  
  print "Case #%i: %s" % ( i, result )
