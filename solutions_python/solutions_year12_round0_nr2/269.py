import sys

if_name, of_name = sys.argv[1:3]

def surp_trip (a):
  a1,a2,a3 = a
  if abs(a1 - a2) == 2 or abs(a2 - a3) == 2 or abs(a3 - a1) == 2:
    return True
  return False

def valid (a):
  a1,a2,a3 = a
  if abs(a1 - a2) <= 2 and abs(a2 - a3) <= 2 and abs(a3 - a1) <= 2:
    return True
  return False

t_s = {}
t_ns = {}
n_s = {}
n_ns = {}
for x1 in range(0,11):
    for x2 in range(0,11):
          for x3 in range(0,11):
                  s = x1+x2+x3
                  t = (x1,x2,x3)
                  if  not valid(t): continue
                  if surp_trip (t):                    
                            if t_s.has_key(s):
                                t_s[s] += [t]
                            else:
                                t_s[s] = [t]
                  else:
                            if t_ns.has_key(s):
                                t_ns[s] += [t]
                            else:
                                t_ns[s] = [t]

ifile = open(if_name,'r')
ofile = open(of_name,'w')

def greater_p (tl,np):
  if tl == []: return False
  if max([max(t) for t in tl]) >= np:
    return True
  return False



for i,ln in enumerate(ifile):
    if i == 0: continue
    ln_s = ln.strip().split()
    ng,ns,p = int(ln_s[0]),int(ln_s[1]),int(ln_s[2])
    tarr = map(int,ln_s[3:])
    sel_ns,sel_s = [],[]
    mval_ns, mval_s =[],[]
    for ti in tarr:
      if greater_p(t_ns[ti],p): 
        mval_ns += [1]
      else: mval_ns += [0]
      if t_s.has_key(ti) and greater_p(t_s[ti],p): mval_s += [1]
      else: mval_s += [0]
    ofile.write("Case #%d: " % i)
    cnt2 = mval_s.count(1)
    res = min(ns,cnt2)
#   change res elements to 1
    temp = 0
    for i,val in enumerate(mval_s):
      if val == 1 and mval_ns[i] == 0: 
        temp += 1    
    for i,val in enumerate(mval_s):
      if val == 1 and mval_ns[i] == 1 and temp < res:
        temp += 1
        mval_ns[i] = 0
        if temp == res: break
    res = min(ng,res+sum(mval_ns))
    ofile.write("%d\n" % (res))
ifile.close()
ofile.close()
