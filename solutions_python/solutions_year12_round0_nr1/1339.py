def decode(filename):
  table = {'\n': '\n', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
  ifile = open(filename, 'rt')
  lines = ifile.readlines()
  ifile.close()
  
  ofile = open('output.txt', 'wt')
  for i in range(1, len(lines)):
    ofile.write("Case #" + str(i) + ": ")
    for char in lines[i]:
      ofile.write(table[char])
  ofile.close()
