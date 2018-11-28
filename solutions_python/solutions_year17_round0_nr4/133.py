# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def coord_to_num(N, R, C):
  return (2 * N) * R + C

def num_to_coord(N, num):
  return (num / (2 * N), num % (2 * N))

def get_new_whole_x_list(N, x_list):
  new_whole_x_list = []
  for x_num in x_list:
    new_whole_x_list.append(x_num)

  row_list = range(1, N + 1)
  column_list = range(1, N + 1)
  for x_num in x_list:
    R, C = num_to_coord(N, x_num)
    row_list.remove(R)
    column_list.remove(C)

  for i in xrange(len(row_list)):
    new_whole_x_list.append(coord_to_num(N, row_list[i], column_list[i]))

  return new_whole_x_list

def get_plus_coord(N, endpoint1, endpoint2):
  # precondition: endpoint1 and endpoint2 are not on the same main diagonal
  smaller = min(endpoint1, endpoint2)
  larger = max(endpoint1, endpoint2)

  R1, C1 = num_to_coord(N, smaller)
  R2, C2 = num_to_coord(N, larger)

  if R1 == 1 and R2 == 1:
    return coord_to_num(N, (R1 - C1 + R2 + C2) / 2, (-R1 + C1 + R2 + C2) / 2)
  if R1 == 1 and R2 == N:
    possible_x, possible_y = (R1 - C1 + R2 + C2) / 2, (-R1 + C1 + R2 + C2) / 2
    if possible_x >= 1 and possible_x <= N and possible_y >= 1 and possible_y <=1:
      return coord_to_num(N, (R1 - C1 + R2 + C2) / 2, (-R1 + C1 + R2 + C2) / 2)
    else:
      return coord_to_num(N, (R1 + C1 + R2 - C2) / 2, (R1 + C1 - R2 + C2) / 2)
  if R1 == N and R2 == N:
    return coord_to_num(N, (R1 + C1 + R2 - C2) / 2, (R1 + C1 - R2 + C2) / 2)

def remove_end_points(N, plus_num, end_points):
  R, C = num_to_coord(N, plus_num)
  # check i + j direction (1, *)
  possible_coord = R + C - 1
  if possible_coord >= 1 and possible_coord <= N:
    if coord_to_num(N, 1, possible_coord) in end_points:
      end_points.remove(coord_to_num(N, 1, possible_coord))
  # check i + j direction (N, *)
  possible_coord = R + C - N
  if possible_coord >= 1 and possible_coord <= N:
    if coord_to_num(N, N, possible_coord) in end_points:
      end_points.remove(coord_to_num(N, N, possible_coord))
  # check i - j direction (1, *)
  possible_coord = -R + C + 1
  if possible_coord >= 1 and possible_coord <= N:
    if coord_to_num(N, 1, possible_coord) in end_points:
      end_points.remove(coord_to_num(N, 1, possible_coord))
  # check i - j direction (N, *)
  possible_coord = -R + C + N
  if possible_coord >= 1 and possible_coord <= N:
    if coord_to_num(N, N, possible_coord) in end_points:
      end_points.remove(coord_to_num(N, N, possible_coord))

  # check i + j direction (*, 1)
  possible_coord = R + C - 1
  if possible_coord >= 1 and possible_coord <= N:
    if coord_to_num(N, possible_coord, 1) in end_points:
      end_points.remove(coord_to_num(N, possible_coord, 1))
  # check i + j direction (*, N)
  possible_coord = R + C - N
  if possible_coord >= 1 and possible_coord <= N:
    if coord_to_num(N, possible_coord, N) in end_points:
      end_points.remove(coord_to_num(N, possible_coord, N))
  # check i - j direction (*, 1)
  possible_coord = R - C + 1
  if possible_coord >= 1 and possible_coord <= N:
    if coord_to_num(N, possible_coord, 1) in end_points:
      end_points.remove(coord_to_num(N, possible_coord, 1))
  # check i - j direction (*, N)
  possible_coord = R - C + N
  if possible_coord >= 1 and possible_coord <= N:
    if coord_to_num(N, possible_coord, N) in end_points:
      end_points.remove(coord_to_num(N, possible_coord, N))

def get_new_whole_plus_list(N, plus_list):
  # pluses removes 2 or 3 or 4 endpoints
  # endpoints: (1, *), (*, 1), (N, *), (*, N)
  # requires N > 1
  new_whole_plus_list = []
  for plus_num in plus_list:
    new_whole_plus_list.append(plus_num)

  end_points = []
  for i in xrange(1, N + 1):
    end_points.append(coord_to_num(N, 1, i))
    end_points.append(coord_to_num(N, N, i))
  for i in xrange(2, N):
    end_points.append(coord_to_num(N, i, 1))
    end_points.append(coord_to_num(N, i, N))

  for plus_num in plus_list:
    remove_end_points(N, plus_num, end_points)

  if coord_to_num(N, 1, 1) in end_points:
    new_plus = coord_to_num(N, 1, 1)
    new_whole_plus_list.append(new_plus)
    remove_end_points(N, new_plus, end_points)

  if coord_to_num(N, 1, N) in end_points:
    new_plus = coord_to_num(N, 1, N)
    new_whole_plus_list.append(new_plus)
    remove_end_points(N, new_plus, end_points)

  while end_points != []:
    new_plus = end_points[0]
    new_whole_plus_list.append(new_plus)
    remove_end_points(N, new_plus, end_points)

  return new_whole_plus_list

def get_whole_dict(x_list, plus_list):
  whole_dict = {}
  for x_num in x_list:
    whole_dict[x_num] = 'x'
  for plus_num in plus_list:
    if plus_num in whole_dict:
      whole_dict[plus_num] = 'o'
    else:
      whole_dict[plus_num] = '+'

  return whole_dict

def fashion_show(N, plus_list, x_list):
  new_whole_x_list = get_new_whole_x_list(N, x_list)
  new_whole_plus_list = get_new_whole_plus_list(N, plus_list)

  whole_dict = get_whole_dict(new_whole_x_list, new_whole_plus_list)

  score = 0
  for coord in whole_dict:
    if whole_dict[coord] == 'o':
      score += 2
    else:
      score += 1
  # remove unchanged original one
  for plus_num in plus_list:
    if whole_dict[plus_num] == '+':
      del whole_dict[plus_num]

  for x_num in x_list:
    if whole_dict[x_num] == 'x':
      del whole_dict[x_num]

  for plus_num in plus_list:
    if plus_num in x_list:
      del whole_dict[plus_num]

  answer_list = []
  for coord in whole_dict:
    R, C = num_to_coord(N, coord)
    answer_list.append((whole_dict[coord], R, C))

  return (score, answer_list)


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  N, M = [int(s) for s in raw_input().split(" ")]  
  plus_list = []
  x_list = []

  for j in xrange(M):
    model_type, R, C = [s for s in raw_input().split(" ")]  
    R = int(R)
    C = int(C)
    if model_type == "o" or model_type == "+":
      plus_list.append(coord_to_num(N, R, C))
    if model_type == "o" or model_type == "x":
      x_list.append(coord_to_num(N, R, C))

  if N > 1:
    score, answer_list = fashion_show(N, plus_list, x_list)
  else:
    if plus_list != [] and x_list != []:
      score = 2
      answer_list = []
    else:
      score = 2
      answer_list = [('o', 1, 1)]

  print "Case #{}: {} {}".format(i, score, len(answer_list))
  for answer in answer_list:
    print "{} {} {}".format(answer[0], answer[1], answer[2])