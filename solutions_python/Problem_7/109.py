f   = open('CropTriangles.in')
out = open('CropTriangles.out' , 'w')

lines = f.readlines()
ncases = int( lines[0].rstrip('\n') )
next = 1

for case in range( ncases ):
  vertices = [ ]
  center = [ 0 ,0 ]
  counter = 0
  data = lines[next+case].rstrip("\n").split(" ")
  n  = int ( data[0] )
  A  = float( data[1] )
  B  = float( data[2] )
  C  = float( data[3] )
  D  = float( data[4] )
  x0 = float( data[5] )
  y0 = float( data[6] ) 
  M  = float( data[7] ) 

  X = x0
  Y = y0
  vertices.append( ( X , Y ) )
  for i in range( n ):
    X = (A * X + B) % M
    Y = (C * Y + D) % M
    vertices.append( ( X , Y ) )

  for i in range ( n ):
    vertex1 = vertices[i]
    for j in range ( i+1 , n ):
      vertex2 = vertices[j]
      for k in range ( j+1 , n ):
        vertex3 = vertices[k]
        for i in range(2):
          center[i] = ( vertex1[i] + vertex2[i] + vertex3[i] ) / 3.0
        if int(center[0]) - center[0] == 0 and int(center[1]) - center[1] == 0:
          counter += 1
  out.write( "Case #%s: %s\n" %( case+1 , counter ) )
