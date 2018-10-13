in_file = 'B-large.in'
out_file = 'B-large.out'

def time_to_number(t):
  h,m = t.strip().split(':')
  return int(h) * 60 + int(m)

def main():
  f = open(in_file)
  of = open(out_file, 'w')
  case_num = int(f.next())
  for i in range(0, case_num):
    t = int(f.next())
    na, nb = f.next().strip().split(' ')
    na = int(na)
    nb = int(nb)
    total = na + nb
    if total == 0:
      of.write("Case #%d: %d %d\r\n" % (i+1, 0, 0))
      continue
    table = []
    for j in range(0, total):
      start, end = f.next().strip().split(' ')
      station = None
      if j < na:
        station = 0
      else:
        station = 1
      table.append((time_to_number(start), time_to_number(end), station))
    table.sort()
    r = [[], []]
    s = [0, 0]
    last = table[0][0]  
    for train in table:
      passed = train[0] - last
      r[0] = [x - passed for x in r[0]]
      r[1] = [x - passed for x in r[1]]
      rs = r[train[2]]
      if len(rs) == 0:
        s[train[2]] = s[train[2]] + 1
        r[1-train[2]].append(train[1]-train[0] + t)
      else:
        found = 0
        for rt in rs:
          if rt <= 0:
            r[1-train[2]].append(train[1]-train[0] + t)
            found = 1
            rs.remove(rt)
            break
        if not found:
          s[train[2]] = s[train[2]] + 1
          r[1-train[2]].append(train[1]-train[0] + t)
      last = train[0] 
    of.write("Case #%d: %d %d\r\n" % (i+1, s[0], s[1]))
  of.close()  


if __name__ == "__main__" : 
  main()