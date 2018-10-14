import math
import pdb

def checkEqual(iterator):
      try:
         iterator = iter(iterator)
         first = next(iterator)
         return all(first == rest for rest in iterator)
      except StopIteration:
         return True
  
def check_col(v_done,r_done,vcols, v_ind):
    if v_done[v_ind] != []:
        return v_done[v_ind]
    v = vcols[v_ind]
    if checkEqual(v):
        v_done[v_ind] = True
        return True
    else:
        v_done[v_ind] = False
        valid_val = max(v)
        retval = True
        for r_ind, elem in enumerate(v):
            if elem != valid_val:
                retval &= check_row(v_done,r_done,vs,vcols,r_ind)
        v_done[v_ind] = retval
        return retval

def check_row(v_done,r_done, vs, vcols, r_ind):
    if r_done[r_ind] != []:
        return r_done[r_ind]
    v = vs[r_ind]
    if checkEqual(v):
        r_done[r_ind] = True
        return True
    else:
        r_done[r_ind] = False
        valid_val = max(v)
        retval = True
        for v_ind, elem in enumerate(v):
            if elem != valid_val:
                retval &= check_col(v_done,r_done,vcols, v_ind)
        r_done[r_ind] = retval
        return retval
                   

def check(vs,n,m):
    vcols = zip(*vs)
    r_done = [[]]*n
    v_done = [[]]*m
    retval = True
    for r_ind in range(len(vs)):
        retval &= check_row(v_done,r_done,vs,vcols,r_ind)
    return retval


infile = open('B-large.in','r')
outfile = open('out.txt','w')
T = int(infile.readline())
for t in range(T):
    print t
    n,m = [int(a) for a in infile.readline().split(' ')]
    vs = []
    for i in range(n):
        vs.append([int(a) for a in infile.readline().split(' ')])
    if check(vs,n,m):
        outfile.write('Case #'+str(t+1)+': YES\n')
        print 'Case #'+str(t+1)+': YES'
    else:
        outfile.write('Case #'+str(t+1)+': NO\n')
        print 'Case #'+str(t+1)+': NO'
infile.close()
outfile.close()
print 'Completed'
                
            
