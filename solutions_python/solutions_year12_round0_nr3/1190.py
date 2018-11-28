def num_digits( x ):
  res = 0
  while x > 0:
    res = res + 1
    x /= 10
  
  return res

def to_int( x ):
  num = 0
  for q in x:
    num = num * 10 + int( q )
  
  return num

f = file( 'f.in' , 'r' )
lines = f.read().split( '\n' )

ntest = int( lines[ 0 ] )
t = 1

output = ''

while t <= ntest:
  line = lines[ t ].split( ' ' )
  a = int( line[ 0 ] )
  b = int( line[ 1 ] )
  d = {}
  
  result = 0
  
  q = a
  while q <= b: 
    if d.has_key( q ) == False:
      cnt = 0
      tmp = list( str( q ) )
      w = 0
      ndigits = num_digits( q )
      while w < ndigits:
	num = to_int( tmp )
	if num >= a and num <= b and d.has_key( num ) == False:
	  cnt += 1
	  d[ num ] = 1
	tmp = tmp[-1:] + tmp[:-1]
	w += 1
     
      result += cnt * (cnt - 1) / 2
    
    q = q + 1
  
  output += 'Case #' + str( t ) + ': ' + str( result ) + '\n'
  t = t + 1

file( 'f.out' , 'w' ).write( output )
