import sys
import fractions

if __name__ == '__main__':
  n_cases = int(sys.stdin.readline())
  current_case = 1
  for case in sys.stdin.readlines():
    ints = [int(x) for x in case.split(' ')]
    c = ints[0]
    ts = sorted(ints[1:])
    
    maxt = ts[1]-ts[0]
    for i in range(2, c):
      maxt = fractions.gcd(maxt, ts[i]-ts[i-1])

    y = 0
    if (ts[-1]%maxt)!=0:
      y = maxt - (ts[-1]%maxt)

    print "Case #%d: %d" % (current_case, y)
    current_case = current_case+1
    

    
