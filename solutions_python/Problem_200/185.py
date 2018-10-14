T = int(input())
for kase in range(T):
  i = input()
  while True:
    keep = False
    for x in range(len(i)-1):
      if i[x] > i[x+1]:
        keep =True
        i = i[:x] + chr(ord(i[x])-1) + '9' * (len(i)-x-1)
        break
    if not keep:
      break
  print("Case #{0}: {1}".format(kase+1,int(i)))

