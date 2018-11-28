nTest=input()
ans=[]
for i in xrange(nTest):
  row=input()
  box=[]
  check=[]
  for j in xrange(4):
    box.append(map(int,raw_input().split()))
  row2=input()
  box2=[]
  for j in xrange(4):
    box2.append(map(int,raw_input().split()))
  check=list(set(box2[row2-1]).intersection (set(box[row-1])))
  if len(check)==1:
    ans.append('Case #'+str(i+1)+': '+str(check[0]))
  elif len(check)>0:
    ans.append('Case #'+str(i+1)+': '+'Bad magician!')
  elif len(check)==0:
    ans.append('Case #'+str(i+1)+': '+'Volunteer cheated!')
for i in ans:
  print i
