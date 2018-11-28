


def getOptimalTime(C,F,X):
  stop=False
  curTime=0.0
  curCookies=0.0
  curRate=2.0
  if X<=C:
    return X/curRate

  while not stop:
    
    #first make C cookies
    timeToC=C/curRate
    curTime+=timeToC
    
    # now to decide whether to buy or not
    timeToGo=(X-C)/curRate
    timeIfBuy=X/(curRate+F)
    
    if timeIfBuy>=timeToGo:
      stop=True
    else:
      curRate+=F

  curTime+=(X-C)/curRate
  return curTime

def main():
  f=open("B-large.in",'r')
  lines=f.readlines()
  lines=lines[1:]
  i=1
  for line in lines:
    line=line.split()
    t=getOptimalTime(float(line[0]),float(line[1]),float(line[2]))
    s="Case #"+str(i)+": "
    s2='{:.7f}'.format(t)
    print s+s2
    i+=1

if __name__=='__main__':
  main()



