import sys   

def main():
  if len(sys.argv)<=1:
      print 'Usage: python C.py <filename>'
      return
  
  arg = sys.argv[1]
  f = open(arg,'r')
  fout = open(arg[:-3]+'out', 'w')
  fr = f.readline()
  fr = fr[:-1]
  for i in range(int(fr)):
    line = f.readline()
    count = 0
    n = line.split()
    for j in range(int(n[0]),int(n[1])):
      strj = str(j)
      tests = []
      for k in range(1,len(strj)):
        test = ''.join([strj[k:],strj[:k]])
        if (int(test) > j and int(test) <= int(n[1]) and test not in tests):
          tests.append(test)
          count += 1
    fout.write("Case #"+str(i+1)+": "+str(count))
    if(i<int(fr)-1):
      fout.write('\n')
  return

if __name__ == '__main__':
  main()