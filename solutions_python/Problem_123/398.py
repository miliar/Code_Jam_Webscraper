# input()
# raw_input().split(' ')
# a,b = [int(x) for x in raw_input().split(' ')]
# R = [int(x[0:-1]) for x in line.split(' ') if x[-1]=='R']

def getNbOps(A, i, Ns, nb_ops, max_ops):
  #print A
  #print Ns[i:]
  if i == len(Ns):
    return nb_ops
  elif Ns[i] < A:
    return getNbOps(A + Ns[i], i+1, Ns, nb_ops, max_ops)
  elif nb_ops > max_ops:
    return max_ops+nb_ops
  else:
    return min(getNbOps(2*A-1, i, Ns, nb_ops+1, len(Ns)-i), nb_ops + len(Ns)-i)

nb_tc = input()

for itc in xrange(nb_tc):
  A,N = [int(x) for x in raw_input().split(' ')]
  Ns = [int(x) for x in raw_input().split(' ')]
  Ns=sorted(Ns)
  nb_op = getNbOps(A, 0, Ns, 0, len(Ns))
  print "Case #%d: %d" % (itc+1, nb_op)
