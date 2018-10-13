def decrypt():
  google = "ynficwlbkuomxsevzpdrjgthaq"
  alpha = "abcdefghijklmnopqrstuvwxyz"
  
  f = open('A-small-attempt0.in', 'r')
  N = f.readline()
  i = 1
  for line in f:
    ans = ""
    line.strip()
    for letter in line:
      if not google.find(letter) == -1:
        ans += alpha[google.find(letter)]
      elif not letter == '\n':
        ans += letter
    print "Case #" + str(i) + ": " + ans
    i += 1
  
decrypt()
