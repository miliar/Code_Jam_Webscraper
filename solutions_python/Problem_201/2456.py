T = int(input())

for i in range(T):
  res = []
  line = input().split()
  nstalls = int(line[0])
  npersons = int(line[1])
  Ls = 0
  Rs = 0
  stalls = ['.']*nstalls
  res = [stalls]
  split = nstalls
  for j in range(npersons-1):
    max_list = max(res, key=len)
    max_index = max(range(len(res)), key=lambda i: res[i])
    if len(max_list) % 2 == 0:
      split = len(max_list)//2
    else:
      split = len(max_list)//2 + 1
    del res[max_index]
    res.insert(max_index, max_list[split:]) 
    res.insert(max_index, max_list[:split-1])
  last_person_stall_choice = max(res, key=len)
  if len(last_person_stall_choice) % 2 == 0:
    last_person_stall = len(last_person_stall_choice)//2
  else:
    last_person_stall = len(last_person_stall_choice)//2 + 1
  Ls = len(last_person_stall_choice[last_person_stall:])
  Rs = len(last_person_stall_choice[:last_person_stall-1])
  print('Case #' + str(i+1) + ':', Ls, Rs)
  