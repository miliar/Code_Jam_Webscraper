from sys import argv

script, in_txt, out_txt = argv

def solver(in_txt, out_txt):
   in_file = open(in_txt)
   out_file = open(out_txt, 'w')
   T = int(in_file.readline())
   for t in range(T):
      N = int(in_file.readline())
      ls = []
      for i in range(4):
         x = map(int, in_file.readline().split())
         ls.append(x)
      f = set(ls[N-1])
      N = int(in_file.readline())
      ls = []
      for i in range(4):
         x = map(int, in_file.readline().split())
         ls.append(x)
      g = set(ls[N-1])
      h = list(f & g)
      if len(h) == 0:
         line = "Case #%d: Volunteer cheated!" % (t+1)
      if len(h) > 1:
         line = "Case #%d: Bad magician!" % (t+1)
      if len(h) == 1:
         line = "Case #%d: %d" % (t+1,h[0])
      out_file.write(line)
      out_file.write('\n')
   in_file.close()
   out_file.close()
   return
   
solver(in_txt, out_txt)
