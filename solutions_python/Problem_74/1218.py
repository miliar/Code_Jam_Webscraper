import sys;


def calc(list):
  ret = 0

  pos = [1, 1]
  for i in xrange(0, len(list)):
    a = list[i][0]
    b = a ^ 1

    move = list[i][1]

    next = pos[b]
    for item in list[i + 1:]:
      if item[0] == b:
        next = item[1]
        break

    diff = abs(move - pos[a]) + 1
    pos[a] = move

    ret += diff
    if next < pos[b]:
      if diff < pos[b] - next:
        pos[b] -= diff
      else:
        pos[b] = next
    else:
      if diff < next - pos[b]:
        pos[b] += diff
      else:
        pos[b] = next
	
#    print "%d: %d %d - %d" % (ret, pos[0], pos[1], a)

  return ret

count = int(sys.stdin.readline());

i=0
for line in sys.stdin:
  if count <= i:
    break
  i += 1
  cmd = line.split(' ')

  item_count = cmd.pop(0)

  target=[]
  for j in xrange(0, int(item_count)):
    if cmd.pop(0) == 'B':
      target.append((0, int(cmd.pop(0))))
    else:
      target.append((1, int(cmd.pop(0))))

  print "Case #%d: %d" % (i, calc(target))
