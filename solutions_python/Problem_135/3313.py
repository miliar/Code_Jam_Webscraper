
def getCard(ro):
  card=[]
  for i in xrange(4):
    r=raw_input()
    row=r.split()
    card.append(row)
  return card[ro]

def test(ca):
  bad="Bad magician!"
  cheat="Volunteer cheated!"
  a=getCard(int(raw_input()) -1)
  b=getCard(int(raw_input()) -1)
  similar=-1
  for i in xrange(0, 4):
    for j in xrange(0, 4):
      if int(a[i]) ==int(b[j]):
        if similar <0: similar=int(b[j])
        else: similar=0
  s=str(similar)
  if similar==0: s=bad
  if similar <0: s=cheat
  print "Case #" +str(ca) +": "+s

t =int(raw_input())
for testNum in range(1, t+1):
  test(testNum)
