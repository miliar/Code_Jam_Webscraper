map = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q': 'z'}

in_file = open('A-small-attempt1.in')
ncases = int(in_file.readline())

out_file = open('output.txt', 'w')

for i in range(0, ncases):
  line = in_file.readline()
  line = line[0:len(line)-1]
  result = ""
  for j in range(0, len(line)):
    result += map[line[j]]
  out_file.write('Case #%d: %s\n' % (i+1, result))
  print result
out_file.close