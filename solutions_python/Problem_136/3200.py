def cookies(c, f, x):
   t = 0
   r = 2
   tend = x / r

   while True:
      t += c / r
      r += f
      new_tend = t + x / r
      if new_tend < tend:
         tend = new_tend
      else:
         break

   return tend

nb_ins = int(raw_input());
for x in range(0, nb_ins):
   ins = raw_input().split(" ")
   print "Case #" + str(x + 1) + ": " + str(cookies(float(ins[0]), float(ins[1]), float(ins[2])))
