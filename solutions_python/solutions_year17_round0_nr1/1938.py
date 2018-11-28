import sys
from pprint import pprint

def get_num_input():
  num = sys.stdin.readline()
  try:
    num = int(num)
  except ValueError:
    print("Error : first line of input is not an int")
    exit()
  return num

def line_to_item(line):
  item = line.split(" ")
  item[1] = int(item[1])
  return item

def is_impossible(item):
  return item[1] > len(item[0])

def is_done(item):
  return item[0].find("-") == -1

#uses the flipper at the begining of the item
def use_flipper(item):
  for i in range(item[1]):
    if(item[0][i] == '+'):
      item[0] = item[0][:i] + "-" + item[0][i+1:]
    elif(item[0][i] == '-'):
      item[0] = item[0][:i] + "+" + item[0][i+1:]
    else:
      print("fatal error on " + str(item[i]))
      exit()
  return item

def compute(item):
  moves = 0
  while(True):
    if is_done(item):
      return moves

    #remove pluses at the beginning
    while(item[0][0] == '+'):
      item[0] = item[0][1:]
    
    if is_impossible(item):
      return -1
    else:
      item = use_flipper(item)
      moves += 1
      

def main():
  num = get_num_input()

  #MAIN LOOP
  i = 0
  for line in sys.stdin:
    i += 1
    print("Case #" + str(i) + ": ", end='')
    item = line_to_item(line)
    ret = compute(item)
    if ret == -1:
      print("IMPOSSIBLE")
    else:
      print(str(ret))

main()    




"""
++--++-- 3
--+-++--
---+-+--
+++-+-++
++++-+-- -> impossible ?

---+-++- 3
++++-++-
-++-
---+
++++ gagné

+++++++++
++---++++
++--+--++
+-+++--++
+-+++-+--
+-++-+---

reso:
+-++-+---
-++-+---
+---+---
---+---
++++---
"""



  
