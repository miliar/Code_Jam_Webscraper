from sys import stdin
read = stdin.readline

ints = lambda:map(int,read().split())
doubles = lambda:map(float,read().split())
def cost(C,F,X,buy):
  cost = 0.
  for b in range(buy):

    cost += C / (2+b*F)
    #print "Cost at step %d: %f (total:%f)" % (b,C / (2+b*F),cost)
  cost += max(0,(X)) / (2+F*buy)
  #print "Total is",cost
  return cost

def one():
  # C = Farm cost
  # F = Cookies/Farm/Second
  # X = Gooooooal! arrriba! Aiaiaiai!
  C,F,X = doubles()
  best = X/2.
  minbuy = 0
  while True:
    laststep = 0
    step = 1
    #print cost(C,F,X,minbuy)
    while cost(C,F,X,minbuy+step) - cost(C,F,X,minbuy+step-1) <= 0:
      minbuy += step
      laststep = step
      step  *= 2
    


    #print minbuy
    if cost(C,F,X,minbuy+1) > cost(C,F,X,minbuy):
      #print "ASSERT minbuy=",minbuy, "||",cost(C,F,X,minbuy), "<", cost(C,F,X,minbuy-1)
      #assert minbuy is 0 or cost(C,F,X,minbuy) < cost(C,F,X,minbuy-1)
      #print "next step is",cost(C,F,X,minbuy+1)
      return cost(C,F,X,minbuy)


  buy = 1
  while True:
    time = cost(C,F,X,buy)
    #print buy-1,best,time
    if time > best:
      return best
    best = time
    buy += 1

T = ints()[0]
for t in range(T):
  result = one()
  print "Case #%d: %.7f" % (t+1,result)