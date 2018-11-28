from string import maketrans
from sys import stdin
from sys import stdout
inp = "abcdefghijklmnopqrstuvwxyz"
out = "yhesocvxduiglbkrztnwjpfmaq"
tab = maketrans(inp,out)
x = input()
y = 1
while y <= x:
  line = stdin.readline()
  stdout.write("Case #" + str(y) + ": " + line.translate(tab))
  y += 1
