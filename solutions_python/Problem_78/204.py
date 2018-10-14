import sys

def solve( filename ):
  file = open( filename, 'r' )
  
  tests = int( file.readline() )
  
  for i in range(tests):
    [n, pd, pg ] = [int(x) for x in file.readline().split()]

    dprint( "Case #{0}: pd {1} pg {2} n {3}".format(i+1, pd, pg, n))

    if pg == 0:
      if pd == 0:
                print( "Case #{0}: {1}".format(i+1, "Possible"))
      else:
                print( "Case #{0}: {1}".format(i+1, "Broken"))

      continue

    if pg == 100:
      if pd == 100:
                print( "Case #{0}: {1}".format(i+1, "Possible"))
      else:
                print( "Case #{0}: {1}".format(i+1, "Broken"))

      continue


    for factor in range(1, n+1):
              if (factor * pd)%100 == 0:
                print( "Case #{0}: {1}".format(i+1, "Possible"))
                break
              if factor==n:
                print( "Case #{0}: {1}".format(i+1, "Broken"))
                dprint( "Case #{0}: {1}".format(i+1, "No n*x"))

def dprint( msg ):
  if 0:
    print(msg)

solve( sys.argv[1] )  
