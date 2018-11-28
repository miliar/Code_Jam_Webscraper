
def test(list):
  for i in range(0, len(list)-1):
    if(valueList[i] > valueList[i+1]):
      return False
  return True

def list2text(list):
  result = "";
  for i in list:
    if(result != "" or i!=0):
      result += str(i)
  if(result == ""):
    result = "0";
  return result

t = int(input())
for line in range(1, t + 1):
  value = input();
  valueList = list(value);

  for i in range(0, len(valueList)):
    valueList[i] = int(valueList[i])

  valueInteger = int(value);
  result = valueInteger
  #print( valueList)
  #phase 1 go from first index to back and stop when fails
  while(not test(valueList)):
    for i in range(0, len(valueList)-1):
      if valueList[i] > valueList[i+1]:
        valueList[i] -= 1
        for j in range(i+1, len(valueList)):
          valueList[j] = 9
        break

  #print(valueList);


  print("Case #{}: {}".format(line, list2text(valueList)));

