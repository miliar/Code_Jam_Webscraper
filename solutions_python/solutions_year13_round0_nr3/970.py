import math

def is_square(apositiveint):
  if apositiveint == 0:
    return True
  if apositiveint == 1:
    return True
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def is_palin(i):
	s = str(i)
	sr = s[::-1]
	if s == sr:
		return True
	else:
		return False
		
	
with open('C-small-attempt1.in') as f:
	next(f)
	with open('output.out', 'w') as f2:
		lineno = 1
		for line in f:
			count=0
			sp = line.split(' ')
			i=int(sp[0])
			j=int(sp[1])
			for r in range (i,j+1):
				if is_palin(r) and is_square(r):
					rr = int(math.sqrt(r))
					
					if is_palin(rr):
						count = count+1
			print("Case #"+str(lineno)+": "+str(count), file=f2)
			lineno = lineno+1