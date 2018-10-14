mappings = {
              'a': 'y',
              'b': 'h',
              'c': 'e',
              'd': 's',
              'e': 'o',
              'f': 'c',
              'g': 'v',
              'h': 'x',
              'i': 'd',
              'j': 'u',
              'k': 'i',
              'l': 'g',
              'm': 'l',
              'n': 'b',
              'o': 'k',
              'p': 'r',
              'q': 'z',
              'r': 't',
              's': 'n',
              't': 'w',
              'u': 'j',
              'v': 'p',
              'w': 'f',
              'x': 'm',
              'y': 'a',
              'z': 'q',
              ' ': ' '
           }

def getMappedData( data ):
  output = ''
  for char in data:
    if char != ' ':
      output += mappings[ char ]
    else:
      output += char
  return output

size = int( input() )
index = 1
while index <= size:
  data = input()
  output = getMappedData( data )
  print( "Case #" + str( index ) + ": " + output )
  index += 1

