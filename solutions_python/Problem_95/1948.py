f=open('inputa.txt','r')
s=f.read()
g=open('outputa.txt','r')
t=g.read()
d={}
for i in range(len(s)):
   d[s[i]]=t[i]
d['q']='z'
d['z']='q'
h=open('ina.txt','r')
r=h.read()
output=''
for i in r:
  output+=d[i]
li=output.split('\n')
li.remove('')
for i,j in enumerate(li):
  print 'Case #%d: %s' % (i+1,j)