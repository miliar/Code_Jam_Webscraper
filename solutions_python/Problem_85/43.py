def works(t, N, A, boost, best):
  time = 0
  for i in range(N):
    distance = A[i]
    if i not in boost:
      inv_speed = 2
    else:
      if time >= t:
        inv_speed = 1 # Booster ready
      elif time + distance * 2 < t:
        inv_speed = 2 # Booster will never be ready
      else:
        time += float(t - time) / 2
        inv_speed = 1
    time += distance * inv_speed
    if best and best <= time:
      return time
  return time

def main():
  T = int(raw_input())
  for test in range(1, T+1):
    A = map(int, raw_input().split())
    L, t, N, C, A = A[0], A[1], A[2], A[3], A[4:]
    A = (A * ((N+C-1)/C))[:N]

    sol = works(t, N, A, set([]), None)
    if L >= 1:
      for i in range(N):
        sol = min(sol, works(t, N, A, set([i]), sol))
    if L >= 2:
      pos = sorted(range(N), key=lambda i: (A[i], i), reverse=True)
      tries = min(100, len(pos))
      for i in range(tries):
        for j in range(i+1, tries):
          sol = min(sol, works(t, N, A, set([pos[i], pos[j]]), sol))
    print "Case #%d: %d" % (test, sol)

if __name__ == '__main__':
  main()
