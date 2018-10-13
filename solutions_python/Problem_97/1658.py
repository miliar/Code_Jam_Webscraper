cases = int( input() )
index = 1
while index <= cases:
    _in = input()
    low,high = _in.split()
    low = int( low )
    high = int( high )
    firstNum = ""
    secondNum = ""
    revNum = ""
    counter = 0
    newNum = ""
    for i in range( low, high + 1 ):
      firstNum = str( i )
      newNum = firstNum
      for j in range( i + 1, high + 1 ):
        if( len( firstNum ) == 1 ):
          break
        secondNum = str( j )
        for k in range( 0, len( firstNum ) ):
          newNum = newNum[ -1 ] + newNum[ : -1 ]
          if not( newNum < firstNum ):
            if newNum == secondNum:
                counter += 1
                break
    print( "Case #" + str( index ) + ": " + str( counter ) )
    counter = 0
    index += 1
