t=input()
for kik in xrange(1,t+1):
  a1=input()
  a1-=1
  t10=map(int,raw_input("").strip().split())
  t11=map(int,raw_input("").strip().split())
  t12=map(int,raw_input("").strip().split())
  t13=map(int,raw_input("").strip().split())
  t1=t10+t11+t12+t13
  ch1=t1[a1*4:a1*4+4]
  a2=input()
  a2-=1
  t20=map(int,raw_input("").strip().split())
  t21=map(int,raw_input("").strip().split())
  t22=map(int,raw_input("").strip().split())
  t23=map(int,raw_input("").strip().split())
  t2=t20+t21+t22+t23
  ch2=t2[a2*4:a2*4+4]
  ch3=list(set(ch1).intersection(ch2))
  if len(ch3)==1:
    print "Case #%r: %r"%(kik,ch3[0])
  elif len(ch3)==0:
    print "Case #%r: Volunteer cheated!"%kik
  else:
    print "Case #%r: Bad magician!"%kik
