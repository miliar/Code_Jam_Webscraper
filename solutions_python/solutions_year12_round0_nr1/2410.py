debugEnabled = False

mapping = {
' ' : ' ',
'a':'y',
'b':'h',
'c':'e',
'd':'s',
'e':'o',
'f':'c',
'g':'v',
'h':'x',
'i':'d',
'j':'u',
'k':'i',
'l':'g',
'm':'l',
'n':'b',
'o':'k',
'p':'r',
'q':'z',
'r':'t',
's':'n',
't':'w',
'u':'j',
'v':'p',
'w':'f',
'x':'m',
'y':'a',
'z':'q',
}

def translate(line,m):
   s = ""
   for char in line:
      if char in mapping:
         mapped = mapping[char]
      else:
         mapped = '?'
      s += mapped

   return s

def doProblem(i, f):
   debug("doing task " + str(i))

   line = f.readline().strip()
   done = translate(line,mapping)
   print "Case #" + str(i+1) + ": " + done

   debug("done task " + str(i))

def debug(m):
   if debugEnabled:
      print(m)

f = open("A-small-attempt0.in",'r')
T = int(f.readline())

debug(str(T) + " tasks")

i = 0
while i < T:
   doProblem(i, f)
   i = i + 1
