#! /usr/bin/python
import math

T = int(raw_input())

for i in range(T):
  print "Case #%d:" % (i+1)

  instr = raw_input().split()
  D = float(instr[0])
  N = int(instr[1])
  A = int(instr[2])

  car_pos = []
  for j in range(N):
    car_pos.append(tuple(map(lambda x: float(x), raw_input().split())))
    

  accels = map(lambda x: float(x), raw_input().split())

  for a in accels:
    
    # preprocess car positions
    p_car_pos = []
    try:
      speeds = []
      for j in range(len(car_pos)):
        try:
          t1 = car_pos[j-1][0]
          d1 = car_pos[j-1][1]
        except IndexError:
          t1 = 0.0
          d1 = 0.0  
        t2 = car_pos[j][0]
        d2 = car_pos[j][1]
        speed = (d2-d1)/(t2-t1)
        speeds.append(speed)

      for j in range(len(car_pos)-1):
        if speeds[j] < speeds[j+1]:
          p_car_pos.append(car_pos[j])

      # cut last distance
      while car_pos[-2][1] > D:
        car_pos.pop()
      if car_pos[-1][1] > D:
        sd = car_pos[-2][1]
        st = car_pos[-2][0]
        fd = car_pos[-1][1]
        ft = car_pos[-1][0]
        dd = fd - sd
        dt = ft - st
        ct = st + ((D-sd)/dd)*dt
        cd = D
        car_pos[-1] = (ct, cd)
    except:
      pass
      

    v = 0.0
    d = 0.0
    t = 0.0
    last_cd = 0.0
    last_ct = 0.0
    for ct, cd in car_pos:
      dt = ct - t
      d1 = v*dt + 0.5*a*dt*dt
      if d1+d > cd: # have to brake to speed of car in front
        t = ct
        d = cd
        #v = (cd-last_cd)/(ct-last_ct)
        v = math.sqrt(v*v + 2*a*(cd-last_cd))
      else:
        d = d1+d
        v = v + a*dt
        t = ct
    
      last_ct = ct
      last_cd = cd
    
    if d != D:
      temp = math.sqrt(v*v - 4*(0.5*a)*(d-D))
      t1 = (-1*v + temp)/a
      t2 = (-1*v - temp)/a
      t += t1
    print t
        
        
