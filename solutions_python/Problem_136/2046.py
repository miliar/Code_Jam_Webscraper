#!/usr/bin/python
def main():
  fin = open('B-large.in','r')
  fout = open('B-large-practice.out','w')
  test_cases = int(fin.readline())
  for test_case in xrange(test_cases):
    win = 0
    cfx = fin.readline().split()
    [C,F,X] = [float(num) for num in cfx]
    rate = 2.0
    cookie = 0.0
    time = 0.0
    while(not win):
      decision = decide(C,X,F,rate,time)
      # print decision
      if decision == 'dont_buy':
        time = time+(X/rate)
        win = 1
      else:
        time = time + (C/rate)
        rate = rate + F
        # print time,rate
    fout.write("Case #%d: %.7f\n"%(test_case+1,time))
  fin.close()
  fout.close()

def decide(c,x,f,rate,time):
  time = 0.0
  if (c/rate)+(x/(rate+f))<(time+(x/rate)):
    return 'buy'
  else:
    return 'dont_buy'
    



if __name__ == '__main__':
  main()