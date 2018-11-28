import sys

#this translator was created by using the hint and the input/output of the
#example
translator = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 
  'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 
  'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 
  't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z' : 'q'}

file = open(sys.argv[1])
G = int(file.readline())

for i, line in enumerate(file):
  new_line = 'Case #' + str(i + 1) + ': '
  for letter in line:
    if letter != '\n':
      new_line += translator[letter]
  print new_line