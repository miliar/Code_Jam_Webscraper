import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'
googlerese = 'yhesocvxduiglbkrztnwjpfmaq'
translate = {}
for i in range(0, len(alphabet)):
   translate[alphabet[i]] = googlerese[i]
count = 0
for test in sys.stdin:
   if count == 0:
      cases = int(test)
      count += 1
      continue
   for i in range(0, len(test)):
      if test[i] != ' ' and test[i] != '\n':
         test = test[0:i] + translate[test[i]] + test[i+1:]

   print "Case #%d: %s" % (count, test.strip())
   count += 1