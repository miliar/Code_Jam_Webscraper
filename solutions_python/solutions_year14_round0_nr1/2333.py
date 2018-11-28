file = open("A-small-attempt1.in")
write = open("result", 'w')
first = True
onlyOne = 0
i = 0
cardRow1 = 0
card = 0
case = 0
for line in file:
  line = line.replace('\n', '')
  if i%5 == 1:
    cardRow1 = int(line)
    case += 1
  if cardRow1 != 0:
    cardRow1 -= 1
  elif first == True and i != 0 and case%2 == 1:
    a = line.split(" ")
    first = False
  elif first == False and case%2 == 0:
    b = line.split(" ")
    first = True
    for n in a:
      if n in b:
        onlyOne += 1
        card = n
    if onlyOne == 1:
      if i%10 != 0:
        write.write("Case #" + str((i//10+1)) + ": " + card + '\n')
      else:
        write.write("Case #" + str((i//10)) + ": " + card + '\n')
      write.flush()
    elif onlyOne == 0:
      if i%10 !=0:
        write.write("Case #" + str(i//10+1) + ": Volunteer cheated!\n")
      else:
        write.write("Case #" + str(i//10) + ": Volunteer cheated!\n")
      write.flush()
    else:
      if i%10 !=0:
        write.write("Case #" + str((i//10+1)) + ": Bad magician!\n")
      else:
        write.write("Case #" + str(i//10) + ": Bad magician!\n")
      write.flush()
    onlyOne = 0
  i += 1
    
