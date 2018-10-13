from sys import argv

script, in_txt, out_txt = argv

def solver(in_txt, out_txt):
   in_file = open(in_txt)
   out_file = open(out_txt, 'w')
   T = int(in_file.readline())
   for t in range(T):
      ls = map(float, in_file.readline().split())
      C, F, X = ls[0], ls[1], ls[2]
      rate = 2.0
      time = 0.0
      while True:
         a = X / rate
         b = (C / rate) + (X / (rate + F))
         if a <= b:
            time += a
            break
         else:
            time += (C / rate) 
            rate += F
      line = "Case #%d: %.7f" % (t+1,time)
      out_file.write(line)
      out_file.write('\n')
   in_file.close()
   out_file.close()
   return
   
   
solver(in_txt, out_txt)
