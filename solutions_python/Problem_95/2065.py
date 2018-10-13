def mapper(string): 
 maps = {"a":"y",
 "b":"h",
 "c":"e",
 "d":"s",
 "e":"o",
 "f":"c",
 "g":"v",
 "h":"x",
 "i":"d",
 "j":"u",
 "k":"i",
 "l":"g",
 "m":"l",
 "n":"b",
 "o":"k",
 "p":"r",
 "q":"z",
 "r":"t",
 "s":"n",
 "t":"w",
 "u":"j",
 "v":"p",
 "w":"f",
 "x":"m",
 "y":"a",
 "z":"q",
 " ":" "
 }
 check = list(string)
 i = 0
 pal = check
 for c in check:
  pal[i] = maps[str(c)]
  i = i + 1
 result = ""
 for c in pal:
  result = result + c
 return str(result)
def main():
 times = input()
 d = []
 for i in range(0,times):
  g = raw_input()
  d.append(g)
 i = 1
 for x in d:
  x = mapper(x)
  print "Case #%d:  %s"%(i,x)
  i = i + 1
if __name__ == "__main__":
 main()
