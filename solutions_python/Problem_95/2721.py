from sys import stdout
googlerese = { 
  "a" : "y",
  "b" : "h",
  "c" : "e",
  "d" : "s",
  "e" : "o",
  "f" : "c",
  "g" : "v",
  "h" : "x",
  "i" : "d",
  "k" : "i",
  "j" : "u",
  "l" : "g",
  "m" : "l",
  "n" : "b",
  "o" : "k",
  "p" : "r",
  "r" : "t",
  "q" : "z",
  "s" : "n",
  "t" : "w",
  "u" : "j",
  "v" : "p",
  "w" : "f",
  "x" : "m",
  "y" : "a",
  "z" : "q",
  " " : " ",
  "\n": "\n",
}
  

f = open("a.in", "r" )
o = open("a.out", "w" )
n = f.readline()
cnt = 1
for line in f:
  out = ""
  for letter in line:
    out += googlerese[ letter ] 
  out = ("Case #{0}: " + out).format(cnt)
  o.write( out )
  cnt += 1
