def r(rowNum):
  numArr = []
  rowsLeft = 4-rowNum
  for k in range(rowNum-1):
    f1.readline()
  nums = (int(s) for s in f1.readline().split())
  for k in nums:
    numArr.append(k)
  for k in range(rowsLeft):
    f1.readline() 
  return numArr

f1 = open("input.txt","r")
f2 = open("output.txt", "w+")
numCases = int(f1.readline())

for i in range(numCases):
  arr1 = []
  arr2 = []
  rowNum1 = int(f1.readline())
  arr1 = r(rowNum1)
  rowNum2 = int(f1.readline())
  arr2 = r(rowNum2)
  arr3 = list(set(arr1) & set(arr2))
  if len(arr3) == 0:
    f2.write("Case #{}: Volunteer Cheated!\n".format(i+1))
  elif len(arr3) == 1:
    f2.write("Case #{}: {}\n".format(i+1, arr3[0]))      
  else:
    f2.write("Case #{}: Bad Magician!\n".format(i+1))
