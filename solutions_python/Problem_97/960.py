import sys, collections


def isRecycled(num1, num2):

      n1 = str(num1)
      n2 = str(num2)
      n1_size = len(n1)

      back = ""
      
      for digit in range(n1_size-1, 0, -1):
            back = n1[digit] + back
            front = n1[0:digit]
            reversed = back + front
            if (int(reversed) == int(num2)):
                  return 1
            
      return 0 



inn = sys.stdin.readline()
cases = int(inn)

for case in range(0, cases):
      
      ab = sys.stdin.readline().split(" ")
      a = int(ab[0])
      b = int(ab[1])
      
      total = 0
      numMap = collections.defaultdict(list)
      
      for num1 in range(a, b+1):
            to_str = ''.join(map(str, sorted(str(num1))))
            numMap[to_str].append(num1)
            
      for num2 in range(a, b+1):
            to_str = ''.join(map(str, sorted(str(num2))))      
            if (numMap[to_str]):
                  for item in numMap[to_str]:
                        
                        if (int(item) != int(num2) and num2 > item  and isRecycled(item, num2)):
                              total += 1
      print "Case #"+str(case+1)+":", total                        