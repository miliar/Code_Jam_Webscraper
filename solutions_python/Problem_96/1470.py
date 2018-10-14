import sys
  
N = sys.stdin.readline()

for case in range(0,int(N)):
  input = [int(x) for x in sys.stdin.readline().split()]
  count = input[0]
  suprises = input[1]  
  p_maximum = input[2]
  res = 0

  for sum in input[3:]:
    mod = sum % 3
    max_with_surp = sum // 3
    max_without_surp = sum // 3

    if mod == 0 : 
      max_with_surp += 1
      max_without_surp += 0
    if mod == 1 : 
      max_with_surp += 1
      max_without_surp += 1
    if mod == 2 : 
      max_with_surp += 2
      max_without_surp += 1

    if sum == 0:
      max_with_surp = 0
      max_without_surp = 0
    if sum == 1:
      max_with_surp = 1
      max_without_surp = 1
    if sum == 2:
      max_with_surp = 2
      max_without_surp = 1
    if sum == 28:
      max_with_surp = 10
      max_without_surp = 10
    if sum == 29 or sum == 30:
      max_with_surp = 10
      max_without_surp = 10

    if p_maximum <= max_without_surp:
      res += 1
    elif p_maximum <= max_with_surp and suprises > 0:
      res += 1
      suprises -= 1

  
  print "Case #%d: %s" % (case+1,res)

