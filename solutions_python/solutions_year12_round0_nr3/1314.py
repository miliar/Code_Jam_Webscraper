import math

f = open( "2", "r" )
l = f.readlines()

tests = int(l[0])

comb = [ 0, 1, 3, 6, 10, 15 ]

def ok( n, m ):
  sn = str(n)
  lsn = len(sn)
  sm = str(m) * 2
  for i in xrange(1, lsn):
    if sm[i:i+lsn] == sn:
      return True
  return False

def ok2( sn, sm ):
  lsn = len(sn)
  sm2 = sm * 2
  for i in xrange(1, lsn):
    if sn[0] == sm2[i] and sm2[i:i+lsn] == sn:
      return True
  return False

for case in xrange(1, tests+1):
  line = l[case].strip()
  a, b = [int(x) for x in line.split( ' ' )]
  t = 0
  f = {}
  g = {}
  o = {}
  for n in xrange( a, b+1 ):
    if not f.has_key( n ):
      sn = str(n)

      #for m in xrange( n+1, b+1 ):
      #  sm = str(m)
      #  if ok2( sn, sm ):
      #    #t += 1
      #    if o.has_key(sn):
      #      o[sn] = "," + sm
      #    else:
      #      o[sn] = sm
      #    if o.has_key(sm):
      #      o[sm] = "," + sn
      #    else:
      #      o[sm] = sn

      f[n] = 'n'
      sn2 = str(n) * 2
      lsn = len(sn)
      lc = []
      for i in xrange(1, lsn):
        c = sn2[i:i+lsn]
        ci = int(c)
        if ci > n and ci >= a and ci <= b and not f.has_key(ci):
          lc.append( ci )
          f[ci] = 'c'
          #print "found", n, " ->", c
      if len(lc) > 0:
        g[str(n)] = lc
        t += comb[len(lc)]
      
  print "Case #%i: %i" % ( case, t )
#  print f
#  for key in g.keys():
#    print key, g[key]
#
#  for key in g.keys():
#    if o.has_key(key):
#      print o[key], " vs", g[key]
#    else:
#      print "MISSING", key, ":", g[key]
