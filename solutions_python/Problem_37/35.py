import logging
###logging.basicConfig(level=logging.DEBUG)
import sys

def getlines(f, x=1):
  lines = []
  for i in xrange(x):
  	lines.append( f.readline().strip() )
  return lines

def getnums(f, num=1):
  lines = getlines(f, num)
  lines = [int(x) for x in lines]
  if num == 1:
  	return lines[0]
  return lines

def getsepnums(f, num=1):
  lines = getlines(f, num)
  lines = [[int(y) for y in x.split()] for x in lines]
  if num == 1:
  	return lines[0]
  return lines

def convertnum(num, base=10):
  temp = []
  i = 0
  while num:
  	temp.append( (num % base) )
  	num /= base
  	i += 1
  return temp[::-1]

def ishappy(num, base):
###  num = list([int(x) for x in str(num)])
  seen = set()
  while num != [1]:
  	logging.info(num)
  	if tuple(num) in seen:
  		return False
  	seen.add( tuple(num) )
  	num = sum( [int(x)**2 for x in num] )
  	num = convertnum(num, base)
  return True

if __name__ == "__main__":
  f = open(sys.argv[1])
  totalcases = getnums(f)
  logging.info("Getting test cases...")
  for casenum in xrange(totalcases):
  	bases = getsepnums(f, 1)
  	i = 2
  	while True:
  		good = True
  		for base in bases:
  			if not ishappy(convertnum(i, base), base):
  				good = False
  				break
  		if good:
  			answer = i
  			break
  		i += 1
  	print "Case #%d: %d" % (casenum+1, answer)
