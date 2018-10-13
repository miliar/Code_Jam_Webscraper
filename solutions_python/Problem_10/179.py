in_file = 'A-large.in'
out_file = 'A-large.out'

def find_max(l):
  max = l[0]
  index = 0
  for i in range(0, len(l)):
    if l[i] > max:
      max = l[i]
      index = i
  return (max, index)    

def main():
  f = open(in_file)
  of = open(out_file, 'w')
  case_num = int(f.next())
  for i in range(0, case_num):
      (p,k,l) = f.next().strip().split(' ')
      p = int(p)
      k = int(k)
      l = int(l)
      keys = f.next().strip().split(' ')
      keys = map(int, keys)
      left = []
      for j in range(0, k):
        left.append(p)
      keys.sort()
      keys.reverse()
      count = 0
      for m in range(0, len(keys)):
        max, index = find_max(left)
        count  = count + keys[m] * (p - max + 1)
        left[index] = left[index] - 1
      of.write("Case #%d: %d\r\n" % (i + 1, count))
  of.close()  


if __name__ == "__main__" : 
  main()