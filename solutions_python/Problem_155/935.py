with open("A-small-attempt1.in") as f:
  num_cases = int(f.readline().strip())
  for case in range(1,num_cases+1):
    data = f.readline().strip().split()
    s_max = int(data[0])
    shy_string = data[1]
    
    total_standing = 0
    invited_guests = 0
    for i in range(len(shy_string)):
      if int(shy_string[i]) == 0:
        continue
      if total_standing >= i:
        # Enough guests already
        total_standing += int(shy_string[i])
      else:
        invited_guests += i - total_standing
        total_standing += invited_guests
        total_standing += int(shy_string[i])
        
    print("Case #{}: {}".format(case, invited_guests))