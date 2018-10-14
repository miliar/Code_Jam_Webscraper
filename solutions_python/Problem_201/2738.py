# Carly Smith
# Google Code Jam 2017
def bathroom_stalls():
  with open('C-small-1-attempt2.in') as f:
    content = f.readlines()

  content = [x.strip("\n") for x in content]

  T = int(content[0])

  for i in range(1,T+1):
    N, K = content[i].split()
    N = int(N)
    K = int(K)

    l, r = find_l_r(N, K)

    print "Case #{0}: {1} {2}".format(i, l, r)

def find_l_r(N, K):
  stalls = [0] * (N + 2)
  stalls[0] = 1
  stalls[N+1] = 1

  free_spots = []
  # up to but not including
  free_spots.append([1, len(stalls) - 1])

  l, r = -1, -1

  for i in range(0,K):
    l, r, free_spots = enter_stall(free_spots)

  return l, r

def enter_stall(free_spots):
  curr_min = -1

  curr_largest = -1
  for i in range(0,len(free_spots)):
    section = free_spots[i]
    if section[1] - section[0] > curr_min:
      curr_largest = i
      curr_min = section[1] - section[0]

  section = free_spots[curr_largest]
  plus = -1
  diff = section[1] - section[0]
  if diff % 2 == 1:
    plus = diff/2 + 1
  else:
    plus = diff/2

  left_section = [section[0], section[0] + plus - 1]
  right_section = [section[0] + plus, section[1]]
  
  one = left_section[1] - left_section[0]
  two = right_section[1] - right_section[0]

  if one < 1:
    free_spots[curr_largest] = right_section
    one = 0
  else:
    #free_spots[curr_largest] = right_section
    #free_spots.insert(curr_largest+1, left_section)
    free_spots[curr_largest] = left_section
    free_spots.insert(curr_largest+1, right_section)

  return max(one, two), min(one, two), free_spots


if __name__ == "__main__":
  bathroom_stalls()
