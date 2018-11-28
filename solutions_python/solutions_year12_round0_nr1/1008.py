import sys
data = sys.stdin.readlines()

conversion = {
  "a" : "y",
  "b" : "h",
  "c" : "e",
  "d" : "s",
  "e" : "o", 
  "f" : "c",
  "g" : "v",
  "h" : "x",
  "i" : "d", 
  "j" : "u",
  "k" : "i",
  "l" : "g",
  "m" : "l",
  "n" : "b",
  "o" : "k",
  "p" : "r",
  "q" : "z",
  "r" : "t",
  "s" : "n",
  "t" : "w",
  "u" : "j",
  "v" : "p",
  "w" : "f",
  "x" : "m",
  "y" : "a",
  "z" : "q", 
  " " : " "
 }

i=1
while ( i < len(data)):
  line = data[i]

  chars = list(line)
  for x in range(len(line)):
    if chars[x] == "\n":
      chars[x] = ""
      continue
    chars[x] = conversion[chars[x]]
  print "Case #" + str(i) + ": " + "".join(chars)
  i=i+1
  
  
