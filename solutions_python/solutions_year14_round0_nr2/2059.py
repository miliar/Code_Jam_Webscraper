def main(f):
  fi = open(f + '.in')
  fo = open(f + '.out', 'w')

  T = int(fi.readline())
  for ti in range(T):
    c, f, x = fi.readline().strip().split(' ')
    c, f, x = float(c), float(f), float(x)
    
    total, l, n, s, r = 0, 100001.0, 2.0, 0.0, int((x/c))
    while True:
      l = s + (x/n)
      s += (c/n)
      n += f
      total = s + (x/n)
      if l < total:
        break


    output = "Case #{}: {:.7f}".format(ti+1, l)
    fo.write(output+"\n")
    print output

if __name__ == "__main__":
  main('B-large')