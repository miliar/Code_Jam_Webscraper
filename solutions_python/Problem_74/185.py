
import string
import re



s = raw_input()
num_r = int(s)
c_num = 0
for r in xrange(num_r):
  c_num +=1
  s = raw_input()
  case = s.split()

  item_num = 0

  blp = 1
  olp = 1
  blat = 0
  olat = 0
  tt = 0

  for item in case:
    item_num += 1
    if item_num == 1:
      continue

    if item_num % 2 == 1:
      next_num = int(item)
      if next_color == "O":
        free = tt - olat
        dist = abs(olp - next_num)

        tt += 1 + max(0, dist - free)
        olp = next_num
        olat = tt
      elif next_color == "B":
        free = tt - blat
        dist = abs(blp - next_num)

        tt += 1 + max(0, dist - free)
        blp = next_num
        blat = tt

    else:
      next_color = item
        
  p_list = []
  p_list.append("Case #")
  p_list.append(str(c_num))
  p_list.append(": ")
  p_list.append(str(tt))
  print ''.join(p_list)



