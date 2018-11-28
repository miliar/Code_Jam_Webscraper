import string

def change(real,unreal,cine,ce,counter):
  for i in range(len(real)):
    if real[i] == cine:
      unreal[i]=ce
      counter +=1
  return (unreal,counter)

def findnext(unreal):
  for i in range(len(unreal)):
    if unreal[i] == "-1":
      return i
  return -1

def baseconvert(number,fromdigits,todigits):
    if str(number)[0]=='-':
        number = str(number)[1:]
        neg=1
    else:
        neg=0

    # make an integer out of the number
    x=long(0)
    for digit in str(number):
       x = x*len(fromdigits) + fromdigits.index(digit)
    
    # create the result in base 'len(todigits)'
    res=""
    while x>0:
        digit = x % len(todigits)
        res = todigits[digit] + res
        x /= len(todigits)
    if neg:
        res = "-"+res

    return res

BASE2 = "0123456789a"
BASE10 = "0123456789"

#print baseconvert("123456789a798465aa",BASE2,BASE10)

f = open("input.in","r")
gg = open("input.out","w")
lat = string.lowercase
basefrom = "0123456789"+lat


a = f.readline().rstrip("\n")
n = int(a)

for tt in range(n):
  b = f.readline().rstrip("\n")

  asoc = {}
  real = []
  unreal = []
  for i in b:
    asoc[i] = 0
    real.append(i)
    unreal.append("-1")

  counter = 0
  (unreal,counter)=change(real,unreal,b[0],1,counter)
  letters = "023456789"+lat
  g = 0

  while counter < len(b):
    m = findnext(unreal)
    (unreal,counter)=change(real,unreal,b[m],letters[g],counter)
    g+=1

  ing = map(lambda(x): str(x),unreal)
  ing = string.join(ing,"")
  bfrom = basefrom[:len(asoc)]
  if len(asoc)!=1:
    ing = baseconvert(ing,bfrom,BASE10)
  else:
    ing = baseconvert(ing,"01",BASE10)
  gg.write("Case #"+str(tt+1)+": "+ing+"\n")
