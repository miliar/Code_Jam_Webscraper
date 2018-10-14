T = int(raw_input())
vowels = set(['a', 'e', 'i', 'o', 'u'])
for t in range(1, T + 1):
  name, n = raw_input().split()
  n = int(n)
  anchors = []
  con_reso = 0
  for i in range(len(name)):
    if name[i] not in vowels:
      con_reso += 1
      if con_reso >= n:
        start = i - n + 1
        anchors.append(start)
    else:
      con_reso = 0
  num = 0
  for step in range(0, len(anchors)):
    for i in range(0, len(anchors)): 
      if i + step >= len(anchors) : break
      start = anchors[i]
      prev_stop = -1
      offset = 0
      if i > 0:
        offset = n - 1
        prev_stop = anchors[i - 1] + n - 1
      left_num = max(0, start - prev_stop - 1 + offset)
      next_start = len(name)
      offset = 0
      if i < len(anchors) - 1 - step:
        offset = n - 1
        next_start = anchors[i + step + 1]
      this_start = anchors[i + step]
      right_num = max(0, next_start - (this_start + n - 1) - 1 + offset)
      num += left_num + right_num + left_num * right_num + 1 
  print "Case #%d: %d" % (t, num) 

