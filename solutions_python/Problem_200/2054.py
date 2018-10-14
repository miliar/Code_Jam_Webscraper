def lol(i):
  for j in range(len(i)-1):
    if(int(i[j])>int(i[j+1])):
      return True
  return False

for i in range(int(input())):
  lst = list(input())
  l = len(lst)
  while(lol(lst)):
    t = l-1
    for j in range(l-1):
      if(lst[j]>lst[j+1]):
        t = j
        break
    l2 = [z for z in lst]
    l2[t] = str(int(l2[t])-1)
    for j in range(t+1,l):
      l2[j] = str(9)
    if(int("".join(l2))<int("".join(lst))):
      lst = [z for z in l2]
    else:
      lst[t] = str(int(lst[t])-1)
  print("".join(lst))
    