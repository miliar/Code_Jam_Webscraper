import math
import sys
import re
ipf = open (sys.argv[1], 'r')
opf = open (sys.argv[2], 'w')
T = int (ipf.readline())
for t in range (1,T+1):
  N = int(ipf.readline())
  mat,wp,lp,np = [],[],[],[]
  owp, oowp = [0.0]*N, [0.0]*N
  for n in range(0,N):
    mat.append(ipf.readline())
    wp.append(mat[n].count('1'))
    lp.append(mat[n].count('0'))
    np.append(mat[n].count('.'))
  wp = map(lambda i: float(wp[i]),range(0,N))
  lp = map(lambda i: float(lp[i]),range(0,N))
  fwp, flp = [0.0]*N,[0.0]*N
  for n in range(0,N):
    fwp[n] = wp[n] / (wp[n] + lp[n])
    flp[n] = wp[n] / (lp[n] + wp[n])
  for n in range(0,N):
    cnt = 0
    idx = 0
    for ch in range(0,N):
      c = mat[n][ch]
      if c!='.':
        if c == '1':
          owp[n] += (wp[idx] / (wp[idx]+lp[idx]-1.0))
        else:
          owp[n] += ((wp[idx]-1.0) /(wp[idx]+lp[idx]-1.0))
        cnt +=1
      idx +=1
    if cnt > 0:
      owp[n] /= float(cnt)
    else:
      owp[n] = 0.0
  print owp
  for n in range(0,N):
    cnt = 0
    idx = 0
    for ch in range(0,N):      
      c = mat[n][ch]
      if c!='.':
        oowp[n] += owp[idx]
        cnt +=1
      idx +=1
    if cnt > 0:
      oowp[n] /= float(cnt)
    else:
      oowp[n] = 0.0
  print oowp
  opf.write("Case #%d:\n" % t)
  print wp 
  for n in range(0,N):
    t1 = (0.25 * fwp[n])
    t2 =(0.5 * owp[n])
    t3 = (0.25*oowp[n])
    rpi = t1 +t2  + t3
    opf.write(str(rpi) + "\n")
ipf.close()
opf.close()
