in_file = 'A-large.in'
out_file = 'A-large.out'

def find_abs (l) :
  min = abs(l[0])
  org = l[0]
  for i in range(0, len(l)):
    if min < abs(l[i]):
      min = abs(l[i])
      org = l[i]
  return org

def remove_number (l, num):
  index = 0
  for i in range(0, len(l)):
    if (l[i] == num):
      index = i
      break
  del l[index]    

def main():
  f = open(in_file)
  of = open(out_file, 'w')
  case_num = int(f.next())
  for i in range(0, case_num):
      numbers = int(f.next())
      x = f.next().strip().split(' ')
      y = f.next().strip().split(' ')
      x = map(int, x)
      y = map(int, y)
      min = 0
      while len(x) > 0 :
        a = find_abs(x)
        max_abs = a
        remove_number(x, a)
        if (max_abs <= 0) :
          y.sort()
          y.reverse()
          ynum = y[0]
        else :
          y.sort()
          ynum = y[0]
        min = min + a * ynum
        remove_number(y, ynum)
      of.write("Case #%d: %d\r\n" % (i + 1, min))
  of.close()  


if __name__ == "__main__" : 
  main()