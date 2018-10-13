import sys

lines = sys.stdin.read().split('\n')

for k in range( 0, int(lines[0]) ):
  line = lines[k+1].split(' ')

  clapping = 0
  needed = 0
  for l in range( 0,len(line[1])):
    #if l-2 <= clapping:
    #  clapping = clapping + int(line[l])
    #else:
    #  needed = needed + l-2-clapping-needed
    if l > clapping + needed:

      needed = l-clapping
    clapping = clapping + int(line[1][l])
  
  sys.stdout.write( 'Case #' + str(k+1) + ': ' )

  print(str( needed ) )
