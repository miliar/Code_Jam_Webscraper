for t in range(input()):
  n, c, m = map(int, raw_input().split())
  tickets = sorted(map(int, raw_input().split()) for _ in range(m))
  rides = 0
  left_tickets = tickets
  while len(left_tickets):
    new_left_tickets = []
    used_cust = set()
    for pos, cust in left_tickets:
      if pos > len(used_cust) and cust not in used_cust:
        used_cust.add(cust)
      else:
        new_left_tickets.append((pos, cust))
    left_tickets = new_left_tickets
    rides += 1
  tickets_by_pos = {p: [] for p in range(1, n+1)}
  for pos, cust in tickets:
    tickets_by_pos[pos].append(cust)
  promoted = 0
  for pos in range(1, n+1):
    if len(tickets_by_pos[pos]) > rides:
      promoted += max(0, len(tickets_by_pos[pos]) - rides)
  print 'Case #%d: %d %d' % (t+1, rides, promoted)
