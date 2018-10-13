def main():
  for case in range(input()):
    n, a, b, c, d, x, y, m = raw_input().split()
    trees = []
    tri = set()
    trees.append((int(x),int(y)))
    for i in range(int(n)-1):
      x = int((int(a)*int(x)+int(b)) % int(m))
      y = int((int(c)*int(y)+int(d)) % int(m))
      trees.append((x,y))
    count1 = 0
    for (x1,y1) in trees:
      count2 = 0
      for (x2,y2) in trees:
        count3 = 0
        for (x3,y3) in trees:
          if (x1 + x2 + x3) % 3 == 0 and (y1 + y2 + y3) % 3 == 0 and ((x1,y1) != (x2,y2)) and ((x2,y2) != (x3,y3)) and ((x3,y3) != (x1,y1)):
            tri.add(str(",".join([str(sorted([count1,count2,count3]))])))
          count3 += 1
        count2 += 1
      count1 += 1
    print 'Case #%s: %s' % (case + 1, len(tri))
main()