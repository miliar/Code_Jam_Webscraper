backward_mappings = {'a': 'y', 'b': 'n', 'c': 'f', 'd': 'i', 'e': 'c', 'f': 'w', 'g': 'l', 'h': 'b', 'i': 'k', 'j': 'u', 'k': 'o', 'l': 'm', 'm': 'x', 'n': 's', 'o': 'e', 'p': 'v', 'q': 'z', 'r': 'p', 's': 'd', 't': 'r', 'u': 'j', 'v': 'g', 'w': 't', 'x': 'h', 'y': 'a', 'z':'q', ' ': ' ' }

mappings = dict([(backward_mappings[k], k) for k in backward_mappings.keys()])

def translate(line):
  newline = ""
  for x in line:
    if x in mappings:
      newline += mappings[x]
    else:
      newline += x
  return newline

lines = []

for x in range(int(raw_input("number of lines: "))):
  lines.append(raw_input(""))

for (i, line) in enumerate(lines):
  print "Case #" + str(i+1) + ": " + translate(line)
