import sys


def do_case(arg1):
  X = int(arg1[0])
  R = int(arg1[1])
  C = int(arg1[2])
  
  if X >= 7 :  return True
  elif X == 1: return False
  if not (R*C)%X == 0: return True
  
  maxoccu1 = (X+1)/2
  maxoccu2 = maxoccu1
  if (X+1)%2 != 0:  maxoccu2+=1
  
  if R>C: (R,C) = (C,R)
  
  if R < maxoccu1 or C < maxoccu2: return True
  
  if X <= 3: return False
  if R == maxoccu1 and C <= maxoccu2+1 : return True
  
  return False


ncases = int(sys.stdin.readline())
for i in range(ncases):
  out="Case #%i: "%(i+1)
  arg1=sys.stdin.readline().rstrip('\n').split(' ')
  
  if do_case(arg1):
    out += 'RICHARD'
  else:
    out += 'GABRIEL'
  print(out)
  