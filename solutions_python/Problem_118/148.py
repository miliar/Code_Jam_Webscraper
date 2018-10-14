import random

def num_digits( i ):
  digits = 1;
  pow10 = 10
  while i >= pow10 :
    digits += 1
    pow10 *= 10
  return digits

def to_base_3(n):
    s=[]
    while n:
        s.append(str(n%3))
        n=n/3
    return ''.join(s[::-1])

def to_base_2(n):
    s=[]
    while n:
        s.append(str(n%2))
        n=n/2
    return ''.join(s[::-1])

def is_pal( i ):
  j = i
  r = []
  while ( j > 0 ) :
    k = j % 10
    r.append(k)
    j /= 10
  r.reverse()
  #print r
  back = 0
  front = len(r)-1
  is_pal = 1
  while ( front > back ) :
    if r[front] != r[back] :
      is_pal = 0
    front += -1
    back += 1
    
  return is_pal


def get_even( n ):
  s1 = to_base_2(n)
  #print s1
  s2 = s1[::-1]
  i1 = int(s1)
  i2 = int(s2)
  nd = num_digits(i1)
  i3 = i1 * pow(10,nd) + i2
  i4 = i3 * i3
  return i3, i4

def get_odd0( n ):
  s1 = to_base_2(n)
  #print s1
  s2 = s1[::-1]
  i1 = int(s1)
  i2 = int(s2)
  nd = num_digits(i1)
  i3 = i1 * pow(10,nd+1) + i2
  i4 = i3 * i3
  return i3, i4

def get_odd1( n ):
  s1 = to_base_2(n)
  #print s1
  s2 = s1[::-1]
  i1 = int(s1)
  i2 = int(s2)
  nd = num_digits(i1)
  i3 = i1 * pow(10,nd+1) + pow(10,nd) + i2
  i4 = i3 * i3
  return i3, i4

def get_odd2( n ):
  s1 = to_base_2(n)
  #print s1
  s2 = s1[::-1]
  i1 = int(s1)
  i2 = int(s2)
  nd = num_digits(i1)
  i3 = i1 * pow(10,nd+1) + 2*pow(10,nd) + i2
  i4 = i3 * i3
  return i3, i4

def process_4_cases( n, flist ) :
  i3, i4 = get_even(n)
  if ( is_pal(i4) ) :
    flist.append(i3)
  i3, i4 = get_odd0(n)
  if ( is_pal(i4) ) :
    flist.append(i3)
  i3, i4 = get_odd1(n)
  if ( is_pal(i4) ) :
    flist.append(i3)
  i3, i4 = get_odd2(n)
  if ( is_pal(i4) ) :
    flist.append(i3)


# n choose 3: + n choose 2 + n choose 1
def get_roots():
  fsroots = [1,2,3]
  for i in range(25):
    w = pow(2,i)
  # n choose 0 :
    n0 = w
    process_4_cases(n0,fsroots)
  
  # n choose 1 :
    for j in range(i):
      x = pow(2,j)
      n1 = w+x
      process_4_cases(n1,fsroots)
  
  # n choose 2 :
      for k in range(j):
        y = pow(2,k)
        n2 = w+x+y
        process_4_cases(n2,fsroots)
  
  # n choose 3 :        
        for l in range(k):
          z = pow(2,l)
          n3 = w+x+y+z
          process_4_cases(n3,fsroots)

    # add 2s:
    s1 = str(2*pow(10,i))
    s2 = s1[::-1]
    i1 = int(s1)
    i2 = int(s2)
    nd = num_digits(i1)
    i3 = i1 * pow(10,nd) + i2
    if ( is_pal(i3*i3) ):
      fsroots.append(i3)
    i3 = i1 * pow(10,nd+1) + i2
    if ( is_pal(i3*i3) ):
      fsroots.append(i3)
    i3 = i1 * pow(10,nd+1) + pow(10,nd) + i2
    if ( is_pal(i3*i3) ):
      fsroots.append(i3)
  return fsroots
  
# main...

#print ">>>"
#for i in range(1,1000000):
#  if is_pal(i) :
#    i2 = i * i
#    if is_pal(i2) :
#      print i, i2
#print ">>>"

def closest_index( a, fairs ):
  n = len(fairs)
  i1 = 0
  i2 = n-1  
  while ( i2 > i1 ):
    mid = (i2-i1)/2 + i1
    if mid == i1 or mid == i2 :
      return mid
    else :
      if a == fairs[mid] :
        return mid
      elif a > fairs[mid] :
        i1 = mid
      else :
        i2 = mid 
        
def get_hits( a, b, fairs):
  ia = closest_index( a, fairs )
  ib = closest_index( b, fairs )
  if fairs[ia] < a :
    ia += 1
  if fairs[ib] > b :
    ib -= 1
  hits = ib-ia+1
  if hits < 0 :
    hits = 0
  return hits

def print_hits( a, b, fairs):
  ia = closest_index( a, fairs )
  ib = closest_index( b, fairs )
  if fairs[ia] < a :
    ia += 1
  if fairs[ib] > b :
    ib -= 1
  hits = ib-ia+1
  if hits < 0 :
    hits = 0
  print a, ia, fsq[ia], fsq[ia+1]
  print b, ib, fsq[ib], fsq[ib+1]
  print "hits = ",hits

print "hi"
roots = get_roots()
roots.sort()
fsq = []
for x in roots:
  print x, x*x
  fsq.append(x*x)
print "num fair = ",len(roots)
#a = random.randint(1,100000000)
#b = a + random.randint(1,1000000000000)
#a = 10 
#b = 120
#a = 1 
#b = 4
a = 1
b = 4
print_hits( a, b, fsq ) 
a = 10
b = 120
print_hits( a, b, fsq ) 
a = 100
b = 1000
print_hits( a, b, fsq ) 
a = 8
b = 485
print_hits( a, b, fsq ) 

f1 = open('g1.dat','r')
s1 = f1.read()
f1.close()
r1 = s1.split('\n')
print r1[0], int (r1[0])
nt = int(r1[0])
print " "
print nt
s2 = ""
for ti in range(1,nt+1) :
  r2 = r1[ti].split()
  #print r2
  a = int(r2[0])
  b = int(r2[1])
  hits = get_hits(a,b,fsq)
  print a, b, " -> ", hits
  s2 += "Case #" + str(ti) + ": " + str(hits) + "\n"

f2 = open('o1.dat','w')
f2.write(s2)
f2.close()
