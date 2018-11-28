def my_log(v):
  d = 2
  iter = 0
  while d <= v:
    iter += 1
    d *= 2
  return iter

def will_win(d, N, P):
  beated = int(my_log(d + 1))
  place = 2**N + 1 - 2 ** (N - beated)
  return place <= P

def can_win(d, N, P):
  return not will_win(2**N - d - 1, N, 2**N - P)


T = input()
for tc in range(1, T+1):
  N, P = [int(x) for x in raw_input().split(" ")]
  peoples = 2**N
  smallest_loser = 2**N + 1
  biggest_winner = 0
  
  sm, lg = 0, 2**N - 1
  
  while sm < lg:
    med = (sm + lg + 1) / 2
    if will_win(med, N, P):
      sm = med
    else:
      lg = med - 1
  print "Case #" + str(tc) + ":", sm,
  sm, lg = 0, 2**N - 1
  while sm < lg:
    med = (sm + lg + 1) / 2
    if can_win(med, N, P):
      sm = med
    else:
      lg = med - 1
  print sm