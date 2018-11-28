import copy
import itertools

colors = {"R":set("R"),"Y":set("Y"),"B":set("B"),"O":set("RY"),"G":set("BY"),"V":set("BR")}

t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
  unis = [int(s) for s in raw_input().split(' ')]
  N = unis[0]
  unicorn = {"R":unis[1],"Y":unis[3],"B":unis[5],"O":unis[2],"G":unis[4],"V":unis[6]}
  if ((unicorn["R"] > unicorn["Y"] + unicorn["B"]) or\
      (unicorn["Y"] > unicorn["R"] + unicorn["B"]) or\
      (unicorn["B"] > unicorn["R"] + unicorn["Y"])):
    res_str = "IMPOSSIBLE"
  else:
    res_str = ""
    first = ""
    prev = ""
#    if ((unicorn["R"] >= unicorn["Y"]) and (unicorn["R"] >= unicorn["B"])):
#      prev = "R"
#      first = "R"
#    if ((unicorn["Y"] >= unicorn["B"]) and (unicorn["Y"] >= unicorn["R"])):
#      prev = "Y"
#      first = "Y"
#    if ((unicorn["B"] >= unicorn["Y"]) and (unicorn["B"] >= unicorn["R"])):
#      prev = "B"
#      first = "B"
    for i in range(N):
      if (prev == ""):
        if ((unicorn["R"] >= unicorn["Y"]) and (unicorn["R"] >= unicorn["B"])):
          res_str += "R"
          prev = "R"
          first = "R"
          unicorn["R"] -= 1
          continue
        if ((unicorn["Y"] >= unicorn["B"]) and (unicorn["Y"] >= unicorn["R"])):
          res_str += "Y"
          prev = "Y"
          first = "Y"
          unicorn["Y"] -= 1
          continue
        if ((unicorn["B"] >= unicorn["Y"]) and (unicorn["B"] >= unicorn["R"])):
          res_str += "B"
          prev = "B"
          first = "B"
          unicorn["B"] -= 1
          continue
      else:
        if (prev == "Y"):
          if ((first <> "Y") and (unicorn[first] > 0)):
            res_str += first
            prev = first
            unicorn[first] -= 1
            continue
          elif (unicorn["R"] >= unicorn["B"]):
            res_str += "R"
            prev = "R"
            unicorn["R"] -= 1
            continue
          else:
            res_str += "B"
            prev = "B"
            unicorn["B"] -= 1
            continue
        if (prev == "R"):
          if ((first <> "R") and (unicorn[first] > 0)):
            res_str += first
            prev = first
            unicorn[first] -= 1
            continue
          elif (unicorn["Y"] >= unicorn["B"]):
            prev = "Y"
            res_str += "Y"
            unicorn["Y"] -= 1
            continue
          else:
            res_str += "B"
            prev = "B"
            unicorn["B"] -= 1
            continue
        if (prev == "B"):
          if ((first <> "B") and (unicorn[first] > 0)):
            res_str += first
            prev = first
            unicorn[first] -= 1
            continue
          elif (unicorn["R"] >= unicorn["Y"]):
            res_str += "R"
            prev = "R"
            unicorn["R"] -= 1
            continue
          else:
            res_str += "Y"
            prev = "Y"
            unicorn["Y"] -= 1
            continue
  case_str = "Case #%d: " %case
  print case_str + res_str
  #print case_str + "%d,%d" %(max_circle,max_pair_circle)
