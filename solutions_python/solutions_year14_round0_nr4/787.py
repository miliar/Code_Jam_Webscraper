from sys import argv

script, in_txt, out_txt = argv

def solver(in_txt, out_txt):
   in_file = open(in_txt)
   out_file = open(out_txt, 'w')
   T = int(in_file.readline())
   for t in range(T):
      N = int(in_file.readline())
      naomi = map(float, in_file.readline().split())
      ken = map(float, in_file.readline().split())
      n1 = naomi[:]
      k1 = ken[:]
      n1.sort(reverse = True)
      profit_1 = 0
      for i in range(N):
         pos = -1
         next = 10
         for j in range(len(k1)):
            if (k1[j] > n1[i]) and (k1[j] < next):
               next = k1[j]
               pos = j
         if pos == -1:
            profit_1 += 1
         else:
            del k1[pos]
      naomi.sort()
      ken.sort(reverse = True)
      profit_2 = 0
      for i in range(N):
         pos = -1
         next = 10
         for j in range(len(naomi)):
            if (naomi[j] > ken[i]) and (naomi[j] < next):
               next = naomi[j]
               pos = j
         if pos == -1:
            del naomi[0]
         else:
            del naomi[pos]
            profit_2 += 1         
      line = "Case #%d: %d %d" % (t+1,profit_2, profit_1)
      out_file.write(line)
      out_file.write('\n')
   in_file.close()
   out_file.close()
   return

solver(in_txt, out_txt)
        
      
