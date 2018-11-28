from codejam import *
from operator import __or__

def subseqs(seq):
    return set(tuple(seq[:N]) for N in irange(1,len(seq)))

fin = open("large.in","r")
fout = open("large.out","w")

C = int(fin.next())
for i_case in irange(1,C):
    N,M = split_ints(fin.next())
    old_dirs = [fin.next().strip().split("/")[1:] for _ in xrange(N)]
    new_dirs = [fin.next().strip().split("/")[1:] for _ in xrange(M)]
    old_paths = reduce(__or__,(subseqs(d) for d in old_dirs),set())
    new_paths = reduce(__or__,(subseqs(d) for d in new_dirs),set())
    ans  = len(new_paths.difference(old_paths))
    fout.write("Case #%i: %i\n"%(i_case,ans))

    
fin.close()
fout.close()