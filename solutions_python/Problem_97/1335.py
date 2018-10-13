for c,l in enumerate(open('C-large.in')):
  if c == 0:
       continue

  A=int(l.split(' ')[0])
  B=int(l.split(' ')[1])

  res=[]
  for n in range(A,B+1):
    
    if len(str(n)) != len(str(A)):
        continue

    t=str(n)

    for i in range(1, len(t)):
        s = t[-i:] + t[:-i] 
        #print i, t, s
        
        m = int(s)
        if len(str(m)) != len(str(A)):
            continue

        if n < m and m <= B:
            res.append(str(n) + '_'+ str(m))


  print 'Case #' + str(c) + ': ' + str(len(set(res)))
  
