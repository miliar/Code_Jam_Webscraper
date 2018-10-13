import copy
import itertools
def key_func(a):
  return a[0]
t = int(input())  # read a line with a single integer
for case in range(1, t + 1):
  cn,jn = [(int(s)) for s in input().split(' ')]
  ca = []
  ja = []
  for i in range(cn):
    ca.append([(int(s)) for s in input().split(' ')])
  for i in range(jn):
    ja.append([(int(s)) for s in input().split(' ')])
  ca = sorted(ca,key=key_func)
  ja = sorted(ja,key=key_func)
  if len(ja):
    jalast = ja[-1][1]
  else:
    jalast = 0
  if len(ca):
    calast = ca[-1][1]
  else:
    calast = 0
  max_time = max(calast,jalast)
  offset = 1440 - max_time
  for i in range(len(ca)):
    ca[i][0] += offset
    ca[i][1] += offset
  for i in range(len(ja)):
    ja[i][0] += offset
    ja[i][1] += offset
  intv = {"c":[],"j":[]}
#  for i in range(len(ca)):
#    if (i == 0):
#      ca_int.append(ca[i][0] - 0)
#    else:
#      ca_int.append(ca[i][0] - ca[i-1][1])
#  ca_int.append(1440 - ca[-1][1])
#  ca_int = sorted(ca_int)
#  for i in range(len(ja)):
#    if (i == 0):
#      ja_int.append(ja[i][0] - 0)
#    else:
#      ja_int.append(ja[i][0] - ja[i-1][1])
#  ja_int.append(1440 - ja[-1][1])
#  ja_int = sorted(ja_int)
  time_table = ["v" for i in range(1440)]
  occu_table = ["v" for i in range(1440)] 
  for act in ca:
    for i in range(act[0],act[1]):
      time_table[i] = "c"
  for act in ja:
    for i in range(act[0],act[1]):
      time_table[i] = "j"
  status = None
  change = 0
  time = {"c":0,"j":0}
  cha_pos = {"c":[],"j":[]}
  for i in range(len(time_table)):
    l = time_table[i]
    if (status == None):
      if (l == "c"):
        status = "c"
        time["c"] += i + 1
        for j in range(i+1):
          occu_table[j] = "c"
      if (l == "j"):
        status = "j"
        time["j"] += i + 1
        for j in range(i+1):
          occu_table[j] = "j"
    else:
      if (l != "v"):
        if (status != l):
          change += 1
          status = l 
          cha_pos[status].append(i)
      time[status] += 1
      occu_table[i] = status 
  time_gap = (time["c"] - time["j"])/2
  if(occu_table[0] != occu_table[-1]):
    change += 1
#  print(occu_table)
#  print(time_table)
#  print(change)
#  print(time["c"])
#  print(time["j"])
  #print(change)
  #print(time_gap)
  if(time_gap > 0):
    even = False
    for p in cha_pos["j"]:
      pos = p - 1
      while(time_table[pos] == "v"):
        time_gap -= 1
        occu_table[pos] = "j"
        if (time_gap == 0):
          even = True
          break
        pos -= 1
      if even:
        break
    if (not even):
      if(occu_table[-1] == "j"):
        pos = 0
        while(time_table[pos] == "v"):
          time_gap -= 1
          occu_table[pos] = "j"
          if (time_gap == 0):
            even = True
            break
          pos += 1
  if(time_gap < 0):
    even = False
    for p in cha_pos["c"]:
      pos = p - 1
      while(time_table[pos] == "v"):
        time_gap += 1
        occu_table[pos] = "c"
        if (time_gap == 0):
          even = True
          break
        pos -= 1
      if even:
        break
    if(not even):
      if(occu_table[-1] == "c"):
        pos = 0
        while(time_table[pos] == "v"):
          time_gap -= 1
          occu_table[pos] = "c"
          if (time_gap == 0):
            even = True
            break
          pos += 1
  #print(time_gap)
  state = None
  start = {"c":0,"j":0}
  for i in range(1440):
    if(state == None):
      if(time_table[i] == "v"):
        state = occu_table[i] 
        start[occu_table[i]] = i
    if(state == "c"):
      if(time_table[i] != "v"):
        intv["c"].append(i-start["c"])
        state = None
        start["c"] = 0
    if(state == "j"):
      if(time_table[i] != "v"):
        intv["j"].append(i-start["j"])
        state = None
        start["j"] = 0
  c_int = sorted(intv["c"],reverse = True)
  j_int = sorted(intv["j"],reverse = True)
  #print(time_gap)
  #print(c_int)
  #print(j_int)
  #print(change)
  if(time_gap > 0):
    for interv in c_int:
      time_gap -= interv
      change += 2
      if time_gap <= 0:
        break
  elif(time_gap < 0):
    for interv in j_int:
      time_gap += interv
      change += 2
      if time_gap >= 0:
        break
  res_str = "%d" %change
  case_str = "Case #%d: " %case
  print(case_str + res_str)
  #print case_str + "%d,%d" %(max_circle,max_pair_circle)
