def main():
   infile = open("B-large.in.txt", 'r')
   outfile = open("out2", 'w')
   for i in range(0, int(infile.readline())):
      r = 2.0
      nextline = infile.readline()
      s = nextline.split()
      c = float(s[0])
      f = float(s[1])
      x = float(s[2])
      t = 0.0
      while calc_time(r, x, t) > calc_time(r+f, x, t+c/r):
         t += c/r
         r += f
         print("t" + str(i) + " = " + str(t))
      time = "%0.7f" % (t+x/r)
      outfile.write("Case #" + str(i+1) + ": " + time + "\n")

def calc_time(r, x, t):
   return x/r + t

if __name__=="__main__":
   main()
