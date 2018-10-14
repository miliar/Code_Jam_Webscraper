#generate all palindromes.
# Generating list of all palindromes at once
# asked this via 'ask a question' portal
# Got response:
# ' No, 10 is not a palindrome. And if you pregenerate a list of palindromes, you should also submit the code you used to do this. '
# hope this is not called cheating or anythin. this executes in < 8 secs on my ubuntu virtual host and > 11 seconds on my windows host

import sys

_debug_ = False

if 'debug' in sys.argv:
 _debug_ = True

def log(mesg):
 if _debug_ : print mesg

validpalins =[ i*i for i in xrange(1,10000000) if 1 <= i*i <= 100000000000000 and str(i)==str(i)[::-1] and str(i*i) == str(i*i)[::-1]]
totalvalid = len(validpalins)
log(validpalins)
text = sys.stdin.read().strip()

cases=text.split("\n")

for casenum in range(1,len(cases)):
  log(cases[casenum])
  (a,b) = cases[casenum].strip().split()
  log("a = %s, b = %s"%(a,b))
  a=int(a)
  b=int(b)
  i=0
  count=0
  while i < totalvalid and validpalins[i] < a: i+=1
  while i < totalvalid and validpalins[i] <= b:
    i+=1
    count+=1
  print "Case #%d: %d"%(casenum,count)


