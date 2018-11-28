import sys

vowels = set( ["a", "e", "i", "o", "u"] )
def solve(name, nVal):
    
  s = 0
  e = 0
  sol = set()
  isCons = True
  for i in range(len(name)):
      if name[i] in vowels:
          s=i+1
          e=i+1
      else:
          e = i+1
          if e-s>nVal:
              s=e-nVal

      #print "%d: s:%d, e:%d - word:%s" % (i,s,e, e-s==nVal-1)

      if e-s == nVal:
          i1 = 0
          while True:
              i2 = e-1
              while True:
                  #print "Substring (%d, %d): %s" % (i1, i2 ,name[i1:i2+1])
                  sol.add( (i1, i2) )
                  i2+=1
                  if i2>=len(name): break
              i1+=1
              if i1>s: break
  #print sol
  return len(sol)
#solve

#print solve("aeiou", 1)
#sys.exit(1)

IN = file(sys.argv[1])

for case in range(int(IN.readline())):
    name, nVal = IN.readline().split()
    #print "Input:#%s#%s" % ( name, nVal)
    print "Case #%d: %d" % (case+1, solve(name, int(nVal)))
