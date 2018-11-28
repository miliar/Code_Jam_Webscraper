def getCommon(arr1,arr2):
  count = 0
  item = 0
  for item1 in arr1:
    for i in range(0,4):
      if item1 == arr2[i]:
	count+=1
	item = item1
  if count == 0:
    return 0
  elif count == 1:
    return item
  return 25


f = open("output.txt","w")
t = int(raw_input())
for i in range(0,t):
  row1 = int(raw_input())
  arr1 = []
  for j in range(0,4):
    arr1.append(list(map(int,raw_input().split())))
  row2 = int(raw_input())
  arr2 = [] 
  for j in range(0,4):
    arr2.append(list(map(int,raw_input().split())))
  common = getCommon(arr1[row1-1],arr2[row2-1])
  f.write("Case #"+str(i+1)+": ");
  if common == 0:
    print "Volunteer cheated!"
    f.write("Volunteer cheated!\n")
  elif common == 25:
    print "Bad magician!"
    f.write("Bad magician!\n")
  else:
    print common
    f.write(str(common)+"\n")
f.close()