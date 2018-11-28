# Author Samvit Majumdar
G = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']
def replace(c):
  return ' ' if c not in G else G[ord(c)-97]
f,o = open('input'),open('output','r+')
l = f.readlines()
a = int(l[0])
for x,s in zip(range(1,a+1),l[1:]):
  j =  'Case #%d: ' % (x,) +''.join(map(replace,list(s))).rstrip()
  o.write(j+'\n')
  print j
o.close()

