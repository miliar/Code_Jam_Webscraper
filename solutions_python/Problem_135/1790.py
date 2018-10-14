import string

f = open("input.in", 'r')
l = f.readlines()
length = int(l.pop(0))

for ind in range(length):
  row1 = int(l.pop(0))
  r1 = l.pop(row1-1)
  del l[0:3]
  row2 = int(l.pop(0))
  r2 = l.pop(row2-1)
  del l[0:3]

  flag = False
  bad = False

  for card2 in r2.split(' '):
    for card1 in r1.split(' '):
        if (int(card1) == int(card2)):
            if (flag == False):
                flag = True
                res = int(card1)
            else:
                bad = True


  if flag == True:
      if bad == False:
          print ("Case #{}: {}".format(ind+1,res))
      else:
          print ("Case #{}: Bad magician!".format(ind+1))
  else:
        print("Case #{}: Volunteer cheated!".format(ind+1))


