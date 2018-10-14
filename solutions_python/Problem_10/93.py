f   = open('TextMessagingOutrage.in')
out = open('TextMessagingOutrage.out' , 'w')

lines = f.readlines()
ncases = int( lines[0].rstrip('\n') )
next = 1

for case in range( ncases ):
  keypad = { }
  data = lines[next].rstrip('\n').split(" ")
  maxlettersperkey = int( data[0] )
  numkeys =  int( data[1] )
  numletters =  int( data[2] )
  next += 1
  freqs = [ int(freq) for freq in lines[next].rstrip('\n').split(" ")]
  next += 1
  
  freqs.sort( reverse=True )
  keypresses = 0
  loop = 0
  while True:
    try:
      for i in range(numkeys):
        keypresses = keypresses + ( freqs[i + loop*numkeys] ) * ( loop + 1 )
      loop = loop + 1
      if loop > maxlettersperkey:
        keypresses = 'Impossible'
        break
    except IndexError:
      break
  
  print "Case #%s: %s" %( case+1 , keypresses )
  out.write( "Case #%s: %s\n" %( case+1 , keypresses ) )