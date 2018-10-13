import sys

def main():
  if len(sys.argv)<=1:
      print 'Usage: python B.py <filename>'
      return
  
  arg = sys.argv[1]
  f = open(arg,'r')
  fout = open(arg[:-3]+'out', 'w')
  fr = f.readline()
  fr = fr[:-1]
  for i in range(int(fr)):
    line = f.readline()
    n = line.split()
    count = 0
    s = int(n[1])
    p = int(n[2])
    if (p == 0):
      count = int(n[0])
    else:  
      for g in range(int(n[0])):
        sc = int(n[g+3])
        if(sc > 0):
          mod = sc % 3
          ms = (sc/3)+mod
          if(mod == 2):
            ms -= 1
          if(ms >= p):
            count += 1
          elif(s > 0 and (mod == 2 or mod == 0)):
            ms += 1
            if(ms >= p):
              count += 1
              s -= 1
    fout.write("Case #"+str(i+1)+": "+str(count))
    if(i<int(fr)-1):
      fout.write('\n')
  return

if __name__ == '__main__':
  main()