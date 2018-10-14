from math import ceil, log


def laske_level(num1, num1amount, num2, num2amount):
  num1 -= 1
  num2 -= 1
  if(num1 < 0):
    num1 = 0;
  if(num2 < 0):
    num2 = 0;

  num1_l = num1 // 2
  num1_r = num1_l
  if(num1 % 2 != 0):
    num1_r += 1

  num2_l = num2 // 2
  num2_r = num2_l
  if(num2 % 2 != 0):
    num2_r += 1

  result1amount = num1amount
  result1 = num1_l
  result2 = 0
  result2amount = 0

  #print("1r {} 1l {} 2r {} 2l {} ".format(num1_r, num1_l, num2_r, num2_l))
  if(num1_r == result1):
    result1amount += num1amount
  else:
    result2amount = num1amount
    result2 = num1_r

  if(num2 != 0):
    if(num2_l == result1):
      result1amount += num2amount
    else:
      result2amount += num2amount
      result2 = num2_l

    if(num2_r == result1):
      result1amount += num2amount
    else:
      result2amount += num2amount
      result2 = num2_r

  return (result1, result1amount, result2, result2amount)




t = int(input())
for line in range(1, t + 1):
  stalls, people = [int(s) for s in input().split(" ")];
  level = (stalls, 1,0,0);
  #print(level);
  people_per_level = 1;
  for i in range(0, 100):
    if(people > people_per_level):
      people -= people_per_level
      people_per_level *= 2
    else:
      if(level[0] < level[2]):
        if(people <= level[3]):
          #using the level[2]
          res_l = (level[2] - 1) // 2
          res_r = res_l
          if((level[2] - 1) % 2 != 0):
            res_r += 1
        else:
          #using the level[0]
          res_l = (level[0] - 1) // 2
          res_r = res_l
          if((level[0] - 1) % 2 != 0):
            res_r += 1
      else:
        if(people <= level[1]):
          #using the level[0]
          res_l = (level[0] - 1) // 2
          res_r = res_l
          if((level[0] - 1) % 2 != 0):
            res_r += 1
        else:
          #using the level[]
          res_l = (level[2] - 1) // 2
          res_r = res_l
          if((level[2] - 1) % 2 != 0):
            res_r += 1
      break;
    level = laske_level(level[0],level[1],level[2],level[3])
    #print(level);
    #print(level[1] + level[3]);
    if(level[0] == 0 and level[2] == 0):
      break



  print("Case #{}: {} {}".format(line, res_r, res_l));

