mapping = {'\n': '\n', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

if __name__ == '__main__':
  import sys
  f = open(str(sys.argv[1]), 'r')
  f.readline()
  i = 1
  for line in f:
    result = ""
    for ch in line:
      result += mapping[ch]
    print "Case #"+str(i)+":"+" "+result[:len(result)-1]
    i += 1

