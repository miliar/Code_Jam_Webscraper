def main():
  for case in range(input()):
    max_l, keys, num = raw_input().split()
    order = sorted(map(int,raw_input().split()))
    count = 0
    level = 1
    
    while level <= int(max_l):
      try:
        for x in range(int(keys)):
          top = order.pop()
          count += int(top) * level
        level += 1
      except:
        break
    
    if len(order) > 0:
      count = "Impossible"
    print 'Case #%s: %s' % (case + 1, count)
main()