import sys

dec_array = 'abcdefghijklmnopqrstuvwxyz'
enc_array = 'yhesocvxduiglbkrztnwjpfmaq'

def googlerese_decode(line):
  total = []
  for char in line:
    if (char == " "):
      total.append(char)
    else:
      index = dec_array.find(char)
      total.append(enc_array[index])
  return "".join(total)

nblines = sys.stdin.readline()
for i in xrange(int(nblines)):
  line = sys.stdin.readline()
  resline = googlerese_decode(line.rstrip('\r\n'))
  print "Case #%s: %s" % (str(i + 1), str(resline))
