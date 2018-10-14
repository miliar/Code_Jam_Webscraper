import sys

def solve( filename ):
  file = open( filename, 'r' )
  
  tests = int( file.readline() )
  
  for i in range(tests):
    [height, width ] = [int(x) for x in file.readline().split()]

    board = []
    for row in range(height):
            board.append( file.readline().strip() )

    possible = 1
    for row in range(height):
            consecutive = 0
            for col in range(width):
                    if board[row][col] == "#":
                            consecutive += 1
                    else:
                            if consecutive%2 != 0:
                                    possible = 0
                            consecutive = 0
            if consecutive%2 != 0:
                                    possible = 0
                    #print( "row {0} col {1} consecutive {2} char {3}".format( row, col, consecutive, board[row][col] ) )


    for col in range(width):
            consecutive = 0
            for row in range(height):
                    if board[row][col] == "#":
                            consecutive += 1
                    else:
                            if consecutive%2 != 0:
                                    possible = 0
                            consecutive = 0

            if consecutive%2 != 0:
                                    possible = 0
                    #print( "row {0} col {1} consecutive {2} char {3}".format( row, col, consecutive, board[row][col] ) )

    if not(possible):
      print( "Case #{0}:".format(i+1))
      print("Impossible")
      continue


    print( "Case #{0}:".format(i+1))
    out = []
    for row in range(height):
            out.append([])
            for col in range(width):
                    if board[row][col] == ".":
                            out[row].append(".")
                    else:
                            if row == 0:
                                      out[row].append("/")
                            else:
                                    if out[row-1][col] == "/":
                                            out[row].append("\\")
                                    else:
                                            out[row].append("/")


    for row in range(height):
            print( "".join(out[row]).replace("//", "@").replace( "\\\\", "$" ).replace("@", "/\\").replace("$","\\/"))
   

solve( sys.argv[1] )  
