import sys

p = sys.argv[1]
f = open(p)
n = int(f.readline())

dd = {}
def r(a,b):
  #if not a in dd:
  #  print a, ":", b
  dd[a] = b

#a = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
#b = 'our language is impossible to understand'
#
#c = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
#d = 'there are twenty six factorial possibilities'
##
#e ='de kr kd eoya kw aej tysr re ujdr lkgc jv'
#f ='so it is okay if you want to just give up'
#
x = "abcdefghijlkmnopqrstuvwxyz \n"
y = "yhesocvxdugilbkrztnwjpfmaq \n"

def pr(x,y):
  for n in range(len(x)):
    r(x[n], y[n])

#pr(a,b)
#pr(c,d)
#pr(e,f)
pr(x,y)

#r('a', '')
#r('b', '')
#r('c', '')
#r('d', '')
#r('e', 'o')
#r('f', '')
#r('g', '')
#r('h', '')
#r('i', '')
#r('j', '')
#r('k', '')
#r('l', '')
#r('m', '')
#r('n', '')
#r('o', '')
#r('p', '')
#r('q', '')
#r('r', '')
#r('s', '')
#r('t', '')
#r('u', '')
#r('v', '')
#r('w', '')
#r('x', '')
#r('y', '')
#r('z', '')

def translate(line):
  return ''.join([dd[x] for x in list(line)])

for l in range(n):
  line = f.readline()
  np = translate(line)
  print "Case #%s: %s" % (l + 1, np),


