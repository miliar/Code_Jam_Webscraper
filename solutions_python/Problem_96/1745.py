def calc(a,p):
    dif=a-3*p
    if dif>=0: return 1
    if dif>=-2 and p>=1: return 1
    if dif>=-4 and p>=2: return 2
    return 0

def solve(s):
    li=s.split(' ',3)
    n=int(li[0])
    s=int(li[1])
    p=int(li[2])
    li=[calc(int(elem),p) for elem in li[3].split(' ')]
    #print li
    return li.count(1)+min(li.count(2),s)

f=open('inb2.txt')
li=f.read().split('\n')
for i,j in enumerate(li):
  if i!=0 and j!='': print 'Case #%d: %d' % (i,solve(j))