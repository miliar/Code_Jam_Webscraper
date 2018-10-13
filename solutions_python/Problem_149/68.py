T = input()

def zamian(aray):
  zamian = 0
  while len(aray)>0:
    pos = aray.index(min(aray))
    ruchow = min(pos,len(aray)-1-pos)
    zamian += ruchow
    del aray[pos]
  return zamian
    

for t in range(1,T+1):
  size = input()
  numbers = map(int,raw_input().split())
  result = zamian(numbers)
  print "Case #"+str(t)+": "+str(result)
