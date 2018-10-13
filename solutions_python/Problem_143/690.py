#!/usr/bin/python
def main():
  fin = open('B-small-attempt0.in','r')
  fout = open('B-small.out','w')
  test_cases = int(fin.readline())
  for test_case in xrange(test_cases):
    [a,b,k] = [int(num) for num in fin.readline().split()]
    old = range(a)
    new = range(b)
    needed = range(k)
    ways = 0
    for x in old:
      for y in new:
        if x&y in needed:
          ways = ways+1
    fout.write("Case #%d: %d\n"%(test_case+1,ways))
  fin.close()
  fout.close()




if __name__ == '__main__':
  main()