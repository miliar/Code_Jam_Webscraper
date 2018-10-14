import sys

cases = int(sys.stdin.readline())

for case in range(1, cases+1):
     row = int(sys.stdin.readline())
     rows= []
     for i in range(0,4):
         rows.append( [ int(x) for x in sys.stdin.readline().split() ] )

     initialrow = rows[row-1]

     row = int(sys.stdin.readline())
     rows= []
     for i in range(0,4):
         rows.append( [ int(x) for x in sys.stdin.readline().split() ] )

     secondrow = rows[row-1]

     intersect = [x for x in initialrow if x in secondrow]

     answer = "Bad magician!"
     if len(intersect) == 1:
         answer = str(intersect[0])
     elif len(intersect) == 0:
         answer = "Volunteer cheated!"


     print ( "Case #" + str(case) + ": " + answer)