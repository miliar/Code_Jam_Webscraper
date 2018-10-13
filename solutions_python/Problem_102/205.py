#20 10    60  30
#10 0     20  10
#25*4     200 50
#24 30 21 150 50
#Case #1: 33.333333 66.666667
#Case #2: 0.000000 100.000000
#Case #3: 25.0 25.0 25.0 25.0
#Case #4: 34.666667 26.666667 38.666667
import sys

def main():
  if len(sys.argv)<=1:
      print 'Usage: python A.py <filename>'
      return
  
  arg = sys.argv[1]
  f = open(arg,'r')
  fout = open(arg[:-3]+'out', 'w')
  fr = f.readline()
  fr = fr[:-1]

  for i in range(int(fr)):
    line = f.readline()
    line = line.split()
    n = int(line.pop(0))
    tot = 0
    mp = 0
    per = []
    rest = 0
    flag = 0
    case = ''
    for j in line:
      tot += int(j)
    mp = float(tot)*2/n
    for j in line:
      p = (mp-float(j))/tot
      per.append(p*100)
    for j in per:
      if (j < 0):
        rest += -j
        flag += 1
    for j in per:
      if(flag):
        if(j < 0):
          j = 0
        else:
          j -= rest/(n-flag)
      case += str(j)+' '
    fout.write('Case #'+str(i+1)+': '+case)
    if(i<int(fr)-1):
      fout.write('\n')
  return

if __name__ == '__main__':
  main()