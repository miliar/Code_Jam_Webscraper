t = input()
store=[]
for a in range(t) :
  count=0
  store = raw_input()
  store = store.strip()
  store = store.split()
  n = int(store.pop(0))
  s = int(store.pop(0))
  p = int(store.pop(0))
  for i in range(len(store)):
    store[i]=int(store[i])
  store.sort()
  prime=0
  for i in range(len(store)):
    if p>=0 and store[i] >= 3*p and store[i]<=30:
      count=len(store)-i
      prime=1
      break
    elif p-1>=0 and store[i] >=3*p-2 :
      count=len(store)-i
      prime=1
      break
  if prime==1:
    i=i-1
  while i >=0 and s>0:
    if p-2>=0 and store[i] >= 3*p-4 :
      s=s-1
      count=count+1
    i=i-1
  if count < 0 :
    count=0
  j=a+1
  j=str(j)
  count=str(count)
  st= 'Case #'+j+': '+count
  print st
