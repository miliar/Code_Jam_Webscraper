#! /usr/local/bin/python3

import sys

input_name = sys.argv[1]
input_file = open( input_name )

T = int( input_file.readline() )

for i in range( T ):
  input_str = input_file.readline()
  S_max, Kth = input_str.split()

  S_max = int( S_max )
  Kth = int( Kth )

  invite_friends = 0
  people = 0

  for k in range( S_max, -1, -1 ):

    people_current = Kth // 10**k
    Kth = Kth % 10**k

    if  ( people_current != 0 ) and ( ( invite_friends + people ) < ( S_max - k ) ):
      invite_friends += S_max - k - people - invite_friends

    if invite_friends == S_max:
      break

    people += people_current

  print( "Case #{0}: {1}".format( i+1, invite_friends ) )
