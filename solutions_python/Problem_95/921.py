import sys

mapping = {'a': 'y','b': 'h','c': 'e','d': 's','e': 'o','f': 'c','g': 'v','h': 'x','i': 'd','j': 'u','k': 'i','l': 'g','m': 'l','n': 'b','o': 'k','p': 'r','q': 'z','r': 't','s': 'n','t': 'w','u': 'j','v': 'p','w': 'f','x': 'm','y': 'a','z': 'q'}


numcases = int(sys.stdin.readline())
for casenumber in xrange(1,numcases+1):
    line = sys.stdin.readline().rstrip("\r\n")
    output = ""
    for char in line:
      if char == ' ':
        output += char
      else:
        output += mapping[char]

    print "Case #%d: %s" % (casenumber, output)

