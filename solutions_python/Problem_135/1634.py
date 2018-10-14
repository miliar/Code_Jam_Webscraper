with open('A-small-attempt1.in', 'r') as f:
   t = int(f.readline())
   for i in xrange(t):
       rowS = int(f.readline())-1
       gridS = []
       for x in xrange(4):
           gridS.append(f.readline().split())
       rowE = int(f.readline())-1
       gridE = []
       for y in xrange(4):
           gridE.append(f.readline().split())
       l = [b for b in gridS[rowS] if b in gridE[rowE]]
       with open('a.out', 'a') as w:
           w.write("Case #%i: %s\n" % (i+1, ("Bad magician!" if len(l) > 1 else (l[0] if len(l) == 1 else "Volunteer cheated!"))))
