t = int(input()) 
for i in range(1, t + 1):
  n = int(input())
  num = list(str(n))
  res = 0
  found = False
  while(n >= 0):
      num = list(str(n))
      if (len(num) == 1):
          res = n
          break
      if(found == True):
          res = n
          break
      for j in range(0,len(num)-1):
            #print(num[j] +", " + num[j+1])
            if (num[j] <= num[j+1]):
                #print(num[j] +", " + num[j+1])
                found = True 
            else:
                #print(num[j] +", " + num[j+1])
                #print(str(j))
                #print(len(num))
                found = False
                for k in range(j+1,len(num)):
                    num[k] = '9'
                while(True):
                    if num[j] == 0:
                        j = j - 1
                        num[j+1] = '9'
                    else:
                        num[j] = chr(int(num[j]) - 1 + 48)
                        break
                break
      num_str = ""
      for l in range(0,len(num)):
          #print(num[l])
          num_str = num_str + num[l] 
      n = int(num_str)      
      #print(n)
  print("Case #{}: {}".format(i, res))
  #break
