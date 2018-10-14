def calSpeed(totald, travelled, speed):
 distance=float(totald-travelled)
 time=distance/speed
 newspeed=totald/time
 return newspeed


def compareSpeed():
  tests = input("")
#print tests
  for test in range(tests):
    totald, horses = [int(s) for s in raw_input().split(" ")]
    minSpeed= 10000
    for f in range(horses):
      travelled, speed = [int(s) for s in raw_input().split(" ")]
      currenthorse=calSpeed(totald, travelled, speed)
      if currenthorse < float(minSpeed):
        minSpeed =currenthorse
    print "Case #" + str(test+1) +": " + '{0:.6f}'.format(minSpeed)
  
compareSpeed()



 
